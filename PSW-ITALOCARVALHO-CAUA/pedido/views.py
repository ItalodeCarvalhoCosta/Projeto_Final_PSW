from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import PedidoForm
from .models import Pedido

TEMPLATE_PEDIDO = "pedido/pedido.html"


def listar_pedidos(request):
    pedidos = Pedido.objects.all()

    return render(
        request,
        TEMPLATE_PEDIDO,
        {
            "pagina": "listar",
            "pedidos": pedidos,
        }
    )


def detalhe_pedido(request, pedido_id):
    pedido = get_object_or_404(
        Pedido,
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


def criar_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        pedido = form.save()
        return HttpResponseRedirect(
            reverse(
                "pedido:detalhe_pedido",
                args=(pedido.id,)
            )
        )

    return render(
        request,
        TEMPLATE_PEDIDO,
        {"pagina": "formulario", "form": form}
    )


def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(
        Pedido,
        pk=pedido_id
    )

    form = PedidoForm(request.POST or None, instance=pedido)
    if form.is_valid():
        pedido = form.save()
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
