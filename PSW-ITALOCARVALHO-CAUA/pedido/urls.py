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
]
