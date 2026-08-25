from django.urls import path

from . import views


app_name = "usuario"

urlpatterns = [
    path(
        "",
        views.listar_usuarios,
        name="listar_usuarios"
    ),
    path(
        "criar/",
        views.criar_usuario,
        name="criar_usuario"
    ),
    path(
        "<int:usuario_id>/",
        views.detalhe_usuario,
        name="detalhe_usuario"
    ),
    path(
        "<int:usuario_id>/editar/",
        views.editar_usuario,
        name="editar_usuario"
    ),
    path(
        "<int:usuario_id>/excluir/",
        views.excluir_usuario,
        name="excluir_usuario"
    ),
]
