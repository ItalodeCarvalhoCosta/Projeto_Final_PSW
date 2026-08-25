from django.db import models
from usuario.models import Usuario


class Pedido(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    bairro = models.CharField(max_length=100)

    rua = models.CharField(max_length=100)

    num_casa = models.CharField(max_length=10)

    cep = models.CharField(max_length=10)

    dataHora = models.DateTimeField()

    descricao_pedido = models.TextField()

    valorTotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
