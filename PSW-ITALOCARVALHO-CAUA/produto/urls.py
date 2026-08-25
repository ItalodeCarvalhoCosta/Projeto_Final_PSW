from django.urls import path

from . import views

app_name = "produto"

urlpatterns = [
    path(
        "categorias/",
        views.listar_categorias,
        name="listar_categorias"
    ),
    path(
        "categorias/criar/",
        views.criar_categoria,
        name="criar_categoria"
    ),
    path(
        "categorias/<int:categoria_id>/",
        views.detalhe_categoria,
        name="detalhe_categoria"
    ),
    path(
        "categorias/<int:categoria_id>/editar/",
        views.editar_categoria,
        name="editar_categoria"
    ),
    path(
        "categorias/<int:categoria_id>/excluir/",
        views.excluir_categoria,
        name="excluir_categoria"
    ),
    path(
        "",
        views.listar_produtos,
        name="listar_produtos"
    ),
    path(
        "criar/",
        views.criar_produto,
        name="criar_produto"
    ),
    path(
        "<int:produto_id>/",
        views.detalhe_produto,
        name="detalhe_produto"
    ),
    path(
        "<int:produto_id>/editar/",
        views.editar_produto,
        name="editar_produto"
    ),
    path(
        "<int:produto_id>/excluir/",
        views.excluir_produto,
        name="excluir_produto"
    ),
]
