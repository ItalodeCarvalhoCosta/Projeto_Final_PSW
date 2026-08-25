from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from usuario.models import Usuario

from .models import Pedido


def listar_pedidos(request):
    pedidos = Pedido.objects.all()

    return render(
        request,
        "pedido/listar_pedidos.html",
        {
            "pedidos": pedidos
        }
    )


def detalhe_pedido(request, pedido_id):
    pedido = get_object_or_404(
        Pedido,
        pk=pedido_id
    )

    return render(
        request,
        "pedido/detalhe_pedido.html",
        {
            "pedido": pedido
        }
    )


def criar_pedido(request):
    usuarios = Usuario.objects.all()

    if request.method == "POST":
        usuario = get_object_or_404(
            Usuario,
            pk=request.POST["usuario"]
        )

        pedido = Pedido.objects.create(
            usuario=usuario,
            bairro=request.POST["bairro"],
            rua=request.POST["rua"],
            num_casa=request.POST["num_casa"],
            cep=request.POST["cep"],
            dataHora=request.POST["dataHora"],
            descricao_pedido=request.POST["descricao_pedido"],
            valorTotal=request.POST["valorTotal"]
        )

        return HttpResponseRedirect(
            reverse(
                "pedido:detalhe_pedido",
                args=(pedido.id,)
            )
        )

    return render(
        request,
        "pedido/formulario_pedido.html",
        {
            "usuarios": usuarios
        }
    )


def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(
        Pedido,
        pk=pedido_id
    )

    usuarios = Usuario.objects.all()

    if request.method == "POST":
        pedido.usuario = get_object_or_404(
            Usuario,
            pk=request.POST["usuario"]
        )

        pedido.bairro = request.POST["bairro"]
        pedido.rua = request.POST["rua"]
        pedido.num_casa = request.POST["num_casa"]
        pedido.cep = request.POST["cep"]
        pedido.dataHora = request.POST["dataHora"]
        pedido.descricao_pedido = request.POST["descricao_pedido"]
        pedido.valorTotal = request.POST["valorTotal"]
        pedido.save()

        return HttpResponseRedirect(
            reverse(
                "pedido:detalhe_pedido",
                args=(pedido.id,)
            )
        )

    return render(
        request,
        "pedido/formulario_pedido.html",
        {
            "pedido": pedido,
            "usuarios": usuarios
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
        "pedido/excluir_pedido.html",
        {
            "pedido": pedido
        }
    )
