from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST
from .forms import CriarUsuarioForm, UsuarioForm
from .models import Usuario
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

TEMPLATE_USUARIO = "usuario/usuario.html"

@login_required
@permission_required("usuario.view_usuario", raise_exception=True)
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
def detalhe_usuario(request, usuario_id):
    if request.user.pk != usuario_id and not request.user.has_perm("usuario.view_usuario"):
        raise PermissionDenied
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
    if request.user.is_authenticated and not request.user.has_perm("usuario.add_usuario"):
        raise PermissionDenied
    form = CriarUsuarioForm(request.POST or None)
    if form.is_valid():
        usuario = form.save()
        if not request.user.is_authenticated:
            return redirect("usuario:login")
        if not request.user.has_perm("usuario.view_usuario"):
            return redirect("produto:catalogo")
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
def editar_usuario(request, usuario_id):
    if request.user.pk != usuario_id and not request.user.has_perm("usuario.change_usuario"):
        raise PermissionDenied
    usuario = get_object_or_404(
        Usuario,
        pk=usuario_id
    )

    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        usuario = form.save()
        if request.user.pk != usuario_id and not request.user.has_perm("usuario.view_usuario"):
            return redirect("produto:catalogo")
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
@permission_required("usuario.delete_usuario", raise_exception=True)
def excluir_usuario(request, usuario_id):
    usuario = get_object_or_404(
        Usuario,
        pk=usuario_id
    )

    if request.method == "POST":
        usuario.delete()
        if request.user.pk == usuario_id:
            logout(request)
            return redirect("inicio")
        if not request.user.has_perm("usuario.view_usuario"):
            return redirect("produto:catalogo")

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
    if request.user.is_authenticated:
        return redirect("produto:catalogo")
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('produto:catalogo')

        else:
            return render(request, 'usuario/login.html', {'error': 'Nome de usuário ou senha inválidos.'})

    return render(request, 'usuario/login.html')

@require_POST
def logout_view(request):
    logout(request)
    return redirect("/")
