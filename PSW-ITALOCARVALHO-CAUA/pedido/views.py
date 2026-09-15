from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import PedidoForm
from .models import Pedido

TEMPLATE_PEDIDO = "pedido/pedido.html"

@login_required
@permission_required("pedido.view_pedido")
def listar_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user)

    return render(
        request,
        "pedido/pedido.html",
        {
            "pedidos": pedidos,
        }
    )

@login_required
@permission_required("pedido.view_pedido")
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

@login_required
@permission_required("pedido.add_pedido")
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

@login_required
@permission_required("pedido.change_pedido")
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

@login_required
@permission_required("pedido.delete_pedido")
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
