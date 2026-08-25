from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import CriarUsuarioForm, UsuarioForm
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
    form = CriarUsuarioForm(request.POST or None)
    if form.is_valid():
        usuario = form.save()
        return HttpResponseRedirect(
            reverse(
                "usuario:detalhe_usuario",
                args=(usuario.id,)
            )
        )

    return render(
        request,
        "usuario/formulario_usuario.html",
        {"form": form}
    )


def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(
        Usuario,
        pk=usuario_id
    )

    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        usuario = form.save()
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
            "form": form,
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
