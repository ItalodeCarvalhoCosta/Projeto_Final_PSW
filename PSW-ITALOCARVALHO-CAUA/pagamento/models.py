from django.db import models
from pedido.models import Pedido


class Pagamento(models.Model):
    pedido = models.OneToOneField(
        Pedido,
        on_delete=models.CASCADE
    )

    formaPagamento = models.CharField(
        max_length=50
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    statusPagamento = models.CharField(
        max_length=50
    )
