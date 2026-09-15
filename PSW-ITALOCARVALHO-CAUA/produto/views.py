from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied  
from functools import wraps
from .forms import CategoriaForm, ProdutoForm
from .models import Categoria, Produto

TEMPLATE_PRODUTO = "produto/produto.html"

# Decorador para permissões de edição e exclusão 
def staff_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return wrapper



def listar_categorias(request):
    categorias = Categoria.objects.all()

    return render(
        request,
        TEMPLATE_PRODUTO,
        {
            "pagina": "listar_categorias",
            "categorias": categorias,
        }
    )


def detalhe_categoria(request, categoria_id):
    categoria = get_object_or_404(
        Categoria,
        pk=categoria_id
    )

    return render(
        request,
        TEMPLATE_PRODUTO,
        {
            "pagina": "detalhe_categoria",
            "categoria": categoria,
        }
    )

@login_required
@staff_required
def criar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(
            reverse("produto:listar_categorias")
        )

    return render(
        request,
        TEMPLATE_PRODUTO,
        {"pagina": "formulario_categoria", "form": form}
    )

@login_required
@staff_required

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(
        Categoria,
        pk=categoria_id
    )

    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        categoria = form.save()
        return HttpResponseRedirect(
            reverse(
                "produto:detalhe_categoria",
                args=(categoria.id,)
            )
        )

    return render(
        request,
        TEMPLATE_PRODUTO,
        {
            "pagina": "formulario_categoria",
            "categoria": categoria,
            "form": form,
        }
    )

@login_required
@staff_required
def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(
        Categoria,
        pk=categoria_id
    )

    if request.method == "POST":
        categoria.delete()

        return HttpResponseRedirect(
            reverse("produto:listar_categorias")
        )

    return render(
        request,
        TEMPLATE_PRODUTO,
        {
            "pagina": "excluir_categoria",
            "categoria": categoria,
        }
    )


def listar_produtos(request):
    produtos = Produto.objects.all()

    return render(
        request,
        TEMPLATE_PRODUTO,
        {
            "pagina": "listar_produtos",
            "produtos": produtos,
        }
    )


def detalhe_produto(request, produto_id):
    produto = get_object_or_404(
        Produto,
        pk=produto_id
    )

    return render(
        request,
        TEMPLATE_PRODUTO,
        {
            "pagina": "detalhe_produto",
            "produto": produto,
        }
    )

@login_required
@staff_required
def criar_produto(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        produto = form.save()
        return HttpResponseRedirect(
            reverse(
                "produto:detalhe_produto",
                args=(produto.id,)
            )
        )

    return render(
        request,
        TEMPLATE_PRODUTO,
        {"pagina": "formulario_produto", "form": form}
    )

@login_required
@staff_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(
        Produto,
        pk=produto_id
    )

    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)
    if form.is_valid():
        produto = form.save()
        return HttpResponseRedirect(
            reverse(
                "produto:detalhe_produto",
                args=(produto.id,)
            )
        )

    return render(
        request,
        TEMPLATE_PRODUTO,
        {
            "pagina": "formulario_produto",
            "produto": produto,
            "form": form,
        }
    )

@login_required
@staff_required
def excluir_produto(request, produto_id):
    produto = get_object_or_404(
        Produto,
        pk=produto_id
    )

    if request.method == "POST":
        produto.delete()

        return HttpResponseRedirect(
            reverse("produto:listar_produtos")
        )

    return render(
        request,
        TEMPLATE_PRODUTO,
        {
            "pagina": "excluir_produto",
            "produto": produto,
        }
    )


@login_required
def catalogo(request):
    produtos = Produto.objects.all()
    return render(
        request,
        "produto/catalogo.html",
        {
            "produtos": produtos
            
        }
    )
