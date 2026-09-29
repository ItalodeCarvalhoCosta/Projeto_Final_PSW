from django.contrib.auth.models import Group, Permission, User
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from pedido.models import Pedido
from produto.models import Categoria, Produto
from .models import Usuario


class AccessTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.customer = Usuario.objects.create_user(
            username="cliente", password="SenhaTeste!482", cpf="111", telefone="111"
        )
        cls.other = Usuario.objects.create_user(
            username="outro", password="SenhaTeste!482", cpf="222", telefone="222"
        )
        cls.admin = User.objects.create_superuser(
            username="admin", password="SenhaTeste!482", email="admin@example.com"
        )
        cls.category = Categoria.objects.create(nome_categoria="Flor", descricao_categoria="Flores")
        cls.product = Produto.objects.create(
            categoria=cls.category, nome_produto="Rosa", descricao_produto="Rosa vermelha",
            precoUnitario="15.00", quantidadeEstoque=10, peso="0.10"
        )
        cls.orders = [Pedido.objects.create(
            numero_pedido=numero,
            usuario=user, bairro="Centro", rua="Rua A", num_casa="1", cep="00000000",
            dataHora=timezone.now(), descricao_pedido="Flores", valorTotal="15.00"
        ) for numero, user in enumerate((cls.customer, cls.other), start=1)]

    def test_public_catalog_and_hidden_management_links(self):
        for name, args in (("produto:catalogo", []), ("produto:listar_produtos", []),
                           ("produto:detalhe_produto", [self.product.pk])):
            response = self.client.get(reverse(name, args=args))
            self.assertContains(response, "Rosa")
            self.assertNotContains(response, reverse("produto:editar_produto", args=[self.product.pk]))
            self.assertNotContains(response, reverse("produto:criar_produto"))

    def test_anonymous_private_routes_require_login(self):
        for url in (reverse("pedido:listar_pedidos"), reverse("usuario:listar_usuarios"),
                    reverse("produto:criar_produto")):
            for method in (self.client.get, self.client.post):
                response = method(url)
                self.assertEqual(response.status_code, 302)
                self.assertTrue(response.url.startswith(reverse("usuario:login") + "?next="))

    def test_customer_cannot_manage_data_by_get_or_post(self):
        self.client.force_login(self.customer)
        routes = [("produto:criar_produto", []), ("produto:editar_produto", [self.product.pk]),
                  ("produto:excluir_produto", [self.product.pk]), ("produto:criar_categoria", []),
                  ("usuario:listar_usuarios", []), ("usuario:editar_usuario", [self.other.pk]),
                  ("usuario:excluir_usuario", [self.other.pk])]
        for order in self.orders:
            routes.extend([("pedido:editar_pedido", [order.pk]), ("pedido:excluir_pedido", [order.pk])])
        for name, args in routes:
            for method in (self.client.get, self.client.post):
                with self.subTest(route=name, args=args, method=method.__name__):
                    self.assertEqual(method(reverse(name, args=args)).status_code, 403)
        self.assertEqual(Pedido.objects.count(), 2)
        self.assertTrue(Produto.objects.filter(pk=self.product.pk).exists())

    def test_customer_sees_only_own_orders(self):
        self.client.force_login(self.customer)
        response = self.client.get(reverse("pedido:listar_pedidos"))
        self.assertQuerySetEqual(response.context["pedidos"], [self.orders[0]])
        self.assertEqual(self.client.get(reverse("pedido:detalhe_pedido", args=[self.orders[0].pk])).status_code, 200)
        self.assertEqual(self.client.get(reverse("pedido:detalhe_pedido", args=[self.orders[1].pk])).status_code, 404)

    def test_customer_group_sees_only_own_orders(self):
        customer_group = Group.objects.create(name="Cliente")
        self.customer.groups.add(customer_group)
        self.client.force_login(self.customer)

        response = self.client.get(reverse("pedido:listar_pedidos"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Meus pedidos")
        self.assertNotContains(response, "Todos os pedidos")
        self.assertQuerySetEqual(response.context["pedidos"], [self.orders[0]])

    def test_order_change_and_delete_permissions_are_limited_to_owner(self):
        self.customer.user_permissions.add(*Permission.objects.filter(
            content_type__app_label="pedido", codename__in=["change_pedido", "delete_pedido"]
        ))
        self.client.force_login(self.customer)
        for route in ("pedido:editar_pedido", "pedido:excluir_pedido"):
            response = self.client.get(reverse(route, args=[self.orders[1].pk]))
            self.assertEqual(response.status_code, 404)

    def test_customer_can_edit_own_profile_without_granting_privileges(self):
        self.client.force_login(self.customer)
        response = self.client.post(reverse("usuario:editar_usuario", args=[self.customer.pk]), {
            "username": "cliente", "first_name": "Nome novo", "cpf": "111", "telefone": "111",
            "is_staff": "on", "is_superuser": "on"
        })
        self.assertEqual(response.status_code, 302)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.first_name, "Nome novo")
        self.assertFalse(self.customer.is_staff)
        self.assertFalse(self.customer.is_superuser)
        self.assertEqual(self.client.get(reverse("usuario:detalhe_usuario", args=[self.other.pk])).status_code, 403)

    def test_admin_sees_all_orders_and_management_forms(self):
        self.client.force_login(self.admin)
        response = self.client.get(reverse("pedido:listar_pedidos"))
        self.assertEqual(response.context["pedidos"].count(), 2)
        for name, args in (("pedido:editar_pedido", [self.orders[0].pk]),
                           ("produto:editar_produto", [self.product.pk]), ("usuario:listar_usuarios", [])):
            self.assertEqual(self.client.get(reverse(name, args=args)).status_code, 200)
        url = reverse("pedido:excluir_pedido", args=[self.orders[0].pk])
        self.assertEqual(self.client.get(url).status_code, 200)
        self.assertTrue(Pedido.objects.filter(pk=self.orders[0].pk).exists())
        self.assertEqual(self.client.post(url).status_code, 302)
        self.assertFalse(Pedido.objects.filter(pk=self.orders[0].pk).exists())

    def test_customer_can_open_checkout_with_items_in_cart(self):
        self.client.force_login(self.customer)
        session = self.client.session
        session["carrinho"] = {str(self.product.pk): 1}
        session.save()
        self.assertContains(self.client.get(reverse("pedido:carrinho")), "Rosa")
        self.assertContains(self.client.get(reverse("pedido:criar_pedido")), 'name="bairro"')

    def test_category_permissions_do_not_allow_product_management(self):
        self.customer.user_permissions.add(*Permission.objects.filter(
            content_type__app_label="produto", codename__in=["change_categoria", "delete_categoria"]
        ))
        self.client.force_login(self.customer)
        for action in ("editar", "excluir"):
            self.assertEqual(self.client.get(reverse(f"produto:{action}_produto", args=[self.product.pk])).status_code, 403)
        self.customer.user_permissions.clear()
        self.customer.user_permissions.add(*Permission.objects.filter(
            content_type__app_label="produto", codename__in=["change_produto", "delete_produto"]
        ))
        for action in ("editar", "excluir"):
            self.assertEqual(self.client.get(reverse(f"produto:{action}_produto", args=[self.product.pk])).status_code, 200)

    def test_staff_flag_alone_does_not_grant_management_permissions(self):
        self.customer.is_staff = True
        self.customer.save(update_fields=["is_staff"])
        self.client.force_login(self.customer)
        self.assertEqual(self.client.get(reverse("produto:criar_produto")).status_code, 403)
        response = self.client.get(reverse("pedido:listar_pedidos"))
        self.assertQuerySetEqual(response.context["pedidos"], [self.orders[0]])

    def test_signup_redirects_to_login_and_creates_unprivileged_account(self):
        Group.objects.create(name="Cliente")
        response = self.client.post(reverse("usuario:criar_usuario"), {
            "username": "novo", "cpf": "333", "telefone": "333",
            "password1": "SenhaTeste!482", "password2": "SenhaTeste!482", "is_superuser": "on"
        })
        self.assertRedirects(response, reverse("usuario:login"))
        account = Usuario.objects.get(username="novo")
        self.assertFalse(account.is_superuser)
        self.assertFalse(account.is_staff)
        self.assertTrue(account.groups.filter(name="Cliente").exists())
        self.assertTrue(Group.objects.filter(name="Cliente").exists())
        self.assertTrue(self.client.login(username="novo", password="SenhaTeste!482"))
        self.assertEqual(self.client.get(reverse("usuario:detalhe_usuario", args=[account.pk])).status_code, 200)

    def test_invalid_login_displays_error(self):
        response = self.client.post(reverse("usuario:login"), {"username": "cliente", "password": "errada"})
        self.assertContains(response, "Nome de usuário ou senha inválidos.")
        self.assertEqual(self.client.post(reverse("usuario:login"), {}).status_code, 200)

    def test_logout_requires_post_and_csrf(self):
        self.client.force_login(self.customer)
        url = reverse("usuario:logout")
        self.assertEqual(self.client.get(url).status_code, 405)
        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.force_login(self.customer)
        self.assertEqual(csrf_client.post(url).status_code, 403)
        csrf_client.get(reverse("produto:catalogo"))
        token = csrf_client.cookies["csrftoken"].value
        self.assertEqual(csrf_client.post(url, {"csrfmiddlewaretoken": token}).status_code, 302)
        self.assertNotIn("_auth_user_id", csrf_client.session)
