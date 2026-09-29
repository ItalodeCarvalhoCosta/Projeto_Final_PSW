from django.urls import path

from . import views


app_name = "pedido"

urlpatterns = [
    path(
        "",
        views.listar_pedidos,
        name="listar_pedidos"
    ),
    path(
        "criar/",
        views.criar_pedido,
        name="criar_pedido"
    ),
    path(
        "<int:pedido_id>/",
        views.detalhe_pedido,
        name="detalhe_pedido"
    ),
    path(
        "<int:pedido_id>/editar/",
        views.editar_pedido,
        name="editar_pedido"
    ),
    path(
        "<int:pedido_id>/excluir/",
        views.excluir_pedido,
        name="excluir_pedido"
    ),
    path(
    "carrinho/",
    views.carrinho,
    name="carrinho"
),


    path(
    "carrinho/adicionar/<int:produto_id>/",
    views.adicionar_carrinho,
    name="adicionar_carrinho"
),
    path(
    "carrinho/aumentar/<int:produto_id>/",
    views.aumentar_quantidade,
    name="aumentar_quantidade"
),


    path(
    "carrinho/diminuir/<int:produto_id>/",
    views.diminuir_quantidade,
    name="diminuir_quantidade"
),
]
