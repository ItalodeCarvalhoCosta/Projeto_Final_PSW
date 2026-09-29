from django.shortcuts import render

from produto.models import Produto


def index(request):
    produtos = Produto.objects.select_related("categoria").order_by("-pk")[:4]
    return render(request, "home/index.html", {"produtos": produtos})
