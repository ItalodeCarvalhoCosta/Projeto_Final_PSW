from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Categoria, Produto


def listar_categorias(request):
    categorias = Categoria.objects.all()

    return render(
        request,
        "produto/listar_categorias.html",
        {
            "categorias": categorias
        }
    )


def detalhe_categoria(request, categoria_id):
    categoria = get_object_or_404(
        Categoria,
        pk=categoria_id
    )

    return render(
        request,
        "produto/detalhe_categoria.html",
        {
            "categoria": categoria
        }
    )


def criar_categoria(request):
    if request.method == "POST":
        Categoria.objects.create(
            nome=request.POST["nome"],
            descricao=request.POST["descricao"]
        )

        return HttpResponseRedirect(
            reverse("produto:listar_categorias")
        )

    return render(
        request,
        "produto/formulario_categoria.html",
        {
            "opcoes": Categoria.NOME_CHOICES
        }
    )


def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(
        Categoria,
        pk=categoria_id
    )

    if request.method == "POST":
        categoria.nome = request.POST["nome"]
        categoria.descricao = request.POST["descricao"]
        categoria.save()

        return HttpResponseRedirect(
            reverse(
                "produto:detalhe_categoria",
                args=(categoria.id,)
            )
        )

    return render(
        request,
        "produto/formulario_categoria.html",
        {
            "categoria": categoria,
            "opcoes": Categoria.NOME_CHOICES
        }
    )


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
        "produto/excluir_categoria.html",
        {
            "categoria": categoria
        }
    )


def listar_produtos(request):
    produtos = Produto.objects.all()

    return render(
        request,
        "produto/listar_produtos.html",
        {
            "produtos": produtos
        }
    )


def detalhe_produto(request, produto_id):
    produto = get_object_or_404(
        Produto,
        pk=produto_id
    )

    return render(
        request,
        "produto/detalhe_produto.html",
        {
            "produto": produto
        }
    )


def criar_produto(request):
    categorias = Categoria.objects.all()

    if request.method == "POST":
        categoria = get_object_or_404(
            Categoria,
            pk=request.POST["categoria"]
        )

        produto = Produto.objects.create(
            categoria=categoria,
            nome=request.POST["nome"],
            descricao=request.POST["descricao"],
            preco=request.POST["preco"],
            estoque=request.POST["estoque"],
            peso=request.POST["peso"],
        )

        return HttpResponseRedirect(
            reverse(
                "produto:detalhe_produto",
                args=(produto.id,)
            )
        )

    return render(
        request,
        "produto/formulario_produto.html",
        {
            "categorias": categorias
        }
    )


def editar_produto(request, produto_id):
    produto = get_object_or_404(
        Produto,
        pk=produto_id
    )

    categorias = Categoria.objects.all()

    if request.method == "POST":
        produto.categoria = get_object_or_404(
            Categoria,
            pk=request.POST["categoria"]
        )

        produto.nome = request.POST["nome"]
        produto.descricao = request.POST["descricao"]
        produto.preco = request.POST["preco"]
        produto.estoque = request.POST["estoque"]
        produto.peso = request.POST["peso"]
        produto.save()

        return HttpResponseRedirect(
            reverse(
                "produto:detalhe_produto",
                args=(produto.id,)
            )
        )

    return render(
        request,
        "produto/formulario_produto.html",
        {
            "produto": produto,
            "categorias": categorias
        }
    )


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
        "produto/excluir_produto.html",
        {
            "produto": produto
        }
    )
