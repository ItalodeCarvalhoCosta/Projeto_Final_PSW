from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Usuario


def listar_usuarios(request):
    usuarios = Usuario.objects.all()

    return render(
        request,
        "usuario/listar_usuarios.html",
        {
            "usuarios": usuarios
        }
    )


def detalhe_usuario(request, usuario_id):
    usuario = get_object_or_404(
        Usuario,
        pk=usuario_id
    )

    return render(
        request,
        "usuario/detalhe_usuario.html",
        {
            "usuario": usuario
        }
    )


def criar_usuario(request):
    users = User.objects.all()

    if request.method == "POST":
        user = get_object_or_404(
            User,
            pk=request.POST["user"]
        )

        usuario = Usuario.objects.create(
            user=user,
            cpf=request.POST["cpf"],
            telefone=request.POST["telefone"]
        )

        return HttpResponseRedirect(
            reverse(
                "usuario:detalhe_usuario",
                args=(usuario.id,)
            )
        )

    return render(
        request,
        "usuario/formulario_usuario.html",
        {
            "users": users
        }
    )


def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(
        Usuario,
        pk=usuario_id
    )

    users = User.objects.all()

    if request.method == "POST":
        usuario.user = get_object_or_404(
            User,
            pk=request.POST["user"]
        )

        usuario.cpf = request.POST["cpf"]
        usuario.telefone = request.POST["telefone"]
        usuario.save()

        return HttpResponseRedirect(
            reverse(
                "usuario:detalhe_usuario",
                args=(usuario.id,)
            )
        )

    return render(
        request,
        "usuario/formulario_usuario.html",
        {
            "usuario": usuario,
            "users": users
        }
    )


def excluir_usuario(request, usuario_id):
    usuario = get_object_or_404(
        Usuario,
        pk=usuario_id
    )

    if request.method == "POST":
        usuario.delete()

        return HttpResponseRedirect(
            reverse("usuario:listar_usuarios")
        )

    return render(
        request,
        "usuario/excluir_usuario.html",
        {
            "usuario": usuario
        }
    )
