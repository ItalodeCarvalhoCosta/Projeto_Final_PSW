from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CriarUsuarioForm, UsuarioForm
from .models import Usuario
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

TEMPLATE_USUARIO = "usuario/usuario.html"

@login_required
@permission_required("usuario.view_usuario")
def listar_usuarios(request):
    usuarios = Usuario.objects.all()

    return render(
        request,
        TEMPLATE_USUARIO,
        {
            "pagina": "listar",
            "usuarios": usuarios,
        }
    )

@login_required
@permission_required("usuario.view_usuario")
def detalhe_usuario(request, usuario_id):
    usuario = get_object_or_404(
        Usuario,
        pk=usuario_id
    )

    return render(
        request,
        TEMPLATE_USUARIO,
        {
            "pagina": "detalhe",
            "usuario": usuario,
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
        TEMPLATE_USUARIO,
        {"pagina": "formulario", "form": form}
    )

@login_required
@permission_required("usuario.change_usuario")
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
        TEMPLATE_USUARIO,
        {
            "pagina": "formulario",
            "usuario": usuario,
            "form": form,
        }
    )

@login_required
@permission_required("usuario.delete_usuario")
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
        TEMPLATE_USUARIO,
        {
            "pagina": "excluir",
            "usuario": usuario,
        }
    )


#login#
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('produto:catalogo')

        else:
            return render(request, 'usuario/login.html', {'error': 'Nome de usuário ou senha inválidos.'})

    return render(request, 'usuario/login.html')

def logout_view(request):
    logout(request)
    return redirect("/")