from django.db import models
from produto.models import Produto
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

    produtos = models.ManyToManyField(
        Produto,
        through="ItemPedido",
        related_name="pedidos"
    )


class ItemPedido(models.Model):
    id_itemPedido = models.AutoField(primary_key=True)

    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name="itens_pedido"
    )

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name="itens"
    )

    quantidade = models.PositiveIntegerField()

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    valorUnit = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} - Pedido {self.pedido_id}"
