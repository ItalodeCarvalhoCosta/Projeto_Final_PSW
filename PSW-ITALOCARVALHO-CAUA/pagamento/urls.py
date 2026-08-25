from django.urls import path

from . import views


app_name = "pagamento"

urlpatterns = [
    path(
        "",
        views.listar_pagamentos,
        name="listar_pagamentos"
    ),
    path(
        "criar/",
        views.criar_pagamento,
        name="criar_pagamento"
    ),
    path(
        "<int:pagamento_id>/",
        views.detalhe_pagamento,
        name="detalhe_pagamento"
    ),
    path(
        "<int:pagamento_id>/editar/",
        views.editar_pagamento,
        name="editar_pagamento"
    ),
    path(
        "<int:pagamento_id>/excluir/",
        views.excluir_pagamento,
        name="excluir_pagamento"
    ),
]
