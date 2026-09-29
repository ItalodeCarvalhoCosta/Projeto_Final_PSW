from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from produto.models import Produto
from .forms import PedidoForm
from .models import Pedido, ItemPedido
from usuario.models import Usuario

TEMPLATE_PEDIDO = "pedido/pedido.html"

@login_required
def listar_pedidos(request):
    pedidos = Pedido.objects.all() if request.user.has_perm("pedido.view_pedido") else Pedido.objects.filter(usuario_id=request.user.pk)

    return render(
        request,
        "pedido/pedido.html",
        {
            "pedidos": pedidos,
            "pagina": "listar",
        }
    )

@login_required
def detalhe_pedido(request, pedido_id):
    pedidos = Pedido.objects.all() if request.user.has_perm("pedido.view_pedido") else Pedido.objects.filter(usuario_id=request.user.pk)
    pedido = get_object_or_404(
        pedidos,
        pk=pedido_id
    )

    return render(
        request,
        TEMPLATE_PEDIDO,
        {
            "pagina": "detalhe",
            "pedido": pedido,
        }
    )

@login_required
@login_required
def criar_pedido(request):

    carrinho = request.session.get("carrinho", {})


    if not carrinho:
        return HttpResponseRedirect(
            reverse("produto:catalogo")
        )


    produtos = Produto.objects.filter(
        id__in=carrinho.keys()
    )


    form = PedidoForm(request.POST or None)


    if form.is_valid():

        pedido = form.save(commit=False)


        pedido.usuario = Usuario.objects.get(
            user_ptr=request.user
        )


        total = 0


        for produto in produtos:

            quantidade = carrinho[str(produto.id)]


            if quantidade > produto.quantidadeEstoque:
                return HttpResponseRedirect(
                    reverse("pedido:carrinho")
                )


            total += produto.precoUnitario * quantidade


        pedido.valorTotal = total


        ultimo_pedido = Pedido.objects.order_by(
            "-numero_pedido"
        ).first()


        if ultimo_pedido:
            pedido.numero_pedido = ultimo_pedido.numero_pedido + 1
        else:
            pedido.numero_pedido = 1


        pedido.save()


        for produto in produtos:

            quantidade = carrinho[str(produto.id)]


            ItemPedido.objects.create(
                pedido=pedido,
                produto=produto,
                quantidade=quantidade,
                valorUnitario=produto.precoUnitario,
                subtotal=produto.precoUnitario * quantidade
            )


            produto.quantidadeEstoque -= quantidade
            produto.save()


        del request.session["carrinho"]


        return HttpResponseRedirect(
            reverse(
                "pedido:detalhe_pedido",
                args=(pedido.id,)
            )
        )


    return render(
        request,
        TEMPLATE_PEDIDO,
        {
            "pagina": "formulario",
            "form": form
        }
    )

@login_required
@permission_required("pedido.change_pedido", raise_exception=True)
def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(
        Pedido,
        pk=pedido_id
    )

    form = PedidoForm(request.POST or None, instance=pedido)
    if form.is_valid():
        pedido = form.save()
        if not request.user.has_perm("pedido.view_pedido") and pedido.usuario_id != request.user.pk:
            return HttpResponseRedirect(reverse("pedido:listar_pedidos"))
        return HttpResponseRedirect(
            reverse(
                "pedido:detalhe_pedido",
                args=(pedido.id,)
            )
        )

    return render(
        request,
        TEMPLATE_PEDIDO,
        {
            "pagina": "formulario",
            "pedido": pedido,
            "form": form,
        }
    )

@login_required
@permission_required("pedido.delete_pedido", raise_exception=True)
def excluir_pedido(request, pedido_id):
    pedido = get_object_or_404(
        Pedido,
        pk=pedido_id
    )

    if request.method == "POST":
        pedido.delete()

        return HttpResponseRedirect(
            reverse("pedido:listar_pedidos")
        )

    return render(
        request,
        TEMPLATE_PEDIDO,
        {
            "pagina": "excluir",
            "pedido": pedido,
        }
    )

def adicionar_carrinho(request, produto_id):

    carrinho = request.session.get("carrinho", {})

    produto = Produto.objects.get(
        id=produto_id
    )

    produto_id = str(produto_id)


    quantidade_atual = carrinho.get(
        produto_id,
        0
    )


    # verifica se ainda tem estoque
    if quantidade_atual + 1 > produto.quantidadeEstoque:
        return HttpResponseRedirect(
            reverse("produto:catalogo")
        )


    # adiciona mais uma unidade
    carrinho[produto_id] = quantidade_atual + 1


    request.session["carrinho"] = carrinho


    return HttpResponseRedirect(
        reverse("produto:catalogo")
    )

def aumentar_quantidade(request, produto_id):

    carrinho = request.session.get("carrinho", {})

    produto_id = str(produto_id)

    if produto_id in carrinho:
        carrinho[produto_id] += 1

    request.session["carrinho"] = carrinho

    return HttpResponseRedirect(
        reverse("pedido:carrinho")
    )

def diminuir_quantidade(request, produto_id):

    carrinho = request.session.get("carrinho", {})

    produto_id = str(produto_id)

    if produto_id in carrinho:

        carrinho[produto_id] -= 1


        if carrinho[produto_id] <= 0:
            del carrinho[produto_id]


    request.session["carrinho"] = carrinho


    return HttpResponseRedirect(
        reverse("pedido:carrinho")
    )

def carrinho(request):

    carrinho = request.session.get(
        "carrinho",
        {}
    )

    produtos = Produto.objects.filter(
        id__in=carrinho.keys()
    )


    itens = []
    total = 0


    for produto in produtos:

        quantidade = carrinho[str(produto.id)]

        subtotal = produto.precoUnitario * quantidade

        total += subtotal


        itens.append(
            {
                "produto":produto,
                "quantidade":quantidade,
                "subtotal":subtotal
            }
        )


    return render(
        request,
        "pedido/carrinho.html",
        {
            "itens":itens,
            "total":total
        }
    )