from django.shortcuts import render, get_object_or_404, redirect

from .models import Categoria, Produto


# ==========================
# CRUD PRODUTO
# ==========================


def listar_produtos(request):

    produtos = Produto.objects.all()

    return render(
        request,
        "produto/listar_produtos.html",
        {
            "produtos": produtos
        }
    )



def detalhe_produto(request, id):

    produto = get_object_or_404(
        Produto,
        id=id
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

        categoria_id = request.POST["categoria"]

        categoria = Categoria.objects.get(
            id=categoria_id
        )

        Produto.objects.create(
            categoria=categoria,
            nome=request.POST["nome"],
            descricao=request.POST["descricao"],
            preco=request.POST["preco"],
            estoque=request.POST["estoque"],
            peso=request.POST["peso"],
            imagem=request.FILES["imagem"]
        )

        return redirect("listar_produtos")


    return render(
        request,
        "produto/criar_produto.html",
        {
            "categorias": categorias
        }
    )



def editar_produto(request, id):

    produto = get_object_or_404(
        Produto,
        id=id
    )

    categorias = Categoria.objects.all()


    if request.method == "POST":

        produto.categoria = Categoria.objects.get(
            id=request.POST["categoria"]
        )

        produto.nome = request.POST["nome"]
        produto.descricao = request.POST["descricao"]
        produto.preco = request.POST["preco"]
        produto.estoque = request.POST["estoque"]
        produto.peso = request.POST["peso"]


        if "imagem" in request.FILES:
            produto.imagem = request.FILES["imagem"]


        produto.save()

        return redirect("listar_produtos")


    return render(
        request,
        "produto/editar_produto.html",
        {
            "produto": produto,
            "categorias": categorias
        }
    )



def excluir_produto(request, id):

    produto = get_object_or_404(
        Produto,
        id=id
    )

    produto.delete()

    return redirect("listar_produtos")