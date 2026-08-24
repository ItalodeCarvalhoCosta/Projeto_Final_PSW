from django.urls import path
from . import views


urlpatterns = [
    path(
        "categorias/",
        views.listar_categorias,
        name="listar_categorias"
    ),

    path(
        "categoria/<int:id>/",
        views.detalhe_categoria,
        name="detalhe_categoria"
    ),

    path(
        "categoria/criar/",
        views.criar_categoria,
        name="criar_categoria"
    ),

    path(
        "categoria/<int:id>/editar/",
        views.editar_categoria,
        name="editar_categoria"
    ),
]