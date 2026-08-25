from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from pedido.models import Pedido

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
    pedidos = Pedido.objects.all()

    if request.method == "POST":
        pedido = get_object_or_404(
            Pedido,
            pk=request.POST["pedido"]
        )

        pagamento = Pagamento.objects.create(
            pedido=pedido,
            formaPagamento=request.POST["formaPagamento"],
            valor=request.POST["valor"],
            statusPagamento=request.POST["statusPagamento"]
        )

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
            "pedidos": pedidos
        }
    )


def editar_pagamento(request, pagamento_id):
    pagamento = get_object_or_404(
        Pagamento,
        pk=pagamento_id
    )

    pedidos = Pedido.objects.all()

    if request.method == "POST":
        pagamento.pedido = get_object_or_404(
            Pedido,
            pk=request.POST["pedido"]
        )

        pagamento.formaPagamento = request.POST["formaPagamento"]
        pagamento.valor = request.POST["valor"]
        pagamento.statusPagamento = request.POST["statusPagamento"]
        pagamento.save()

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
            "pedidos": pedidos
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
