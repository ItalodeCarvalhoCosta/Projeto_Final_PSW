from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import PagamentoForm
from .models import Pagamento


def listar_pagamentos(request):
    pagamentos = Pagamento.objects.all()

    return render(
        request,
        "pagamento/listar_pagamentos.html",
        {
            "pagamentos": pagamentos
        }
    )


def detalhe_pagamento(request, pagamento_id):
    pagamento = get_object_or_404(
        Pagamento,
        pk=pagamento_id
    )

    return render(
        request,
        "pagamento/detalhe_pagamento.html",
        {
            "pagamento": pagamento
        }
    )


def criar_pagamento(request):
    form = PagamentoForm(request.POST or None)
    if form.is_valid():
        pagamento = form.save()
        return HttpResponseRedirect(
            reverse(
                "pagamento:detalhe_pagamento",
                args=(pagamento.id,)
            )
        )

    return render(
        request,
        "pagamento/formulario_pagamento.html",
        {"form": form}
    )


def editar_pagamento(request, pagamento_id):
    pagamento = get_object_or_404(
        Pagamento,
        pk=pagamento_id
    )

    form = PagamentoForm(request.POST or None, instance=pagamento)
    if form.is_valid():
        pagamento = form.save()
        return HttpResponseRedirect(
            reverse(
                "pagamento:detalhe_pagamento",
                args=(pagamento.id,)
            )
        )

    return render(
        request,
        "pagamento/formulario_pagamento.html",
        {
            "pagamento": pagamento,
            "form": form,
        }
    )


def excluir_pagamento(request, pagamento_id):
    pagamento = get_object_or_404(
        Pagamento,
        pk=pagamento_id
    )

    if request.method == "POST":
        pagamento.delete()

        return HttpResponseRedirect(
            reverse("pagamento:listar_pagamentos")
        )

    return render(
        request,
        "pagamento/excluir_pagamento.html",
        {
            "pagamento": pagamento
        }
    )
