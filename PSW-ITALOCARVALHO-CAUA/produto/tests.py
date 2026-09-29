from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .forms import ProdutoForm
from .models import Categoria


class CategoriaCreationTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_superuser(
			username="gerente", email="gerente@example.com", password="SenhaTeste!482"
		)
		self.client.force_login(self.user)

	def test_create_category_accepts_a_custom_name(self):
		response = self.client.get(reverse("produto:criar_categoria"))
		self.assertContains(response, 'name="nome_categoria"')
		self.assertContains(response, 'type="text"')

		response = self.client.post(reverse("produto:criar_categoria"), {
			"nome_categoria": "Plantas tropicais",
			"descricao_categoria": "Plantas para ambientes internos",
		})

		self.assertRedirects(response, reverse("produto:listar_categorias"))
		self.assertTrue(Categoria.objects.filter(nome_categoria="Plantas tropicais").exists())

	def test_product_form_keeps_existing_category_selection(self):
		category = Categoria.objects.create(
			nome_categoria="Plantas tropicais", descricao_categoria="Plantas de interior"
		)

		self.assertIn(category, ProdutoForm().fields["categoria"].queryset)
