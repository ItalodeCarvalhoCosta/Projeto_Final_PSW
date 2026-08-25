import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pedido", "0001_initial"),
        ("produto", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemPedido",
            fields=[
                (
                    "id_itemPedido",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("quantidade", models.PositiveIntegerField()),
                (
                    "subtotal",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "valorUnit",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itens",
                        to="pedido.pedido",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itens_pedido",
                        to="produto.produto",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="pedido",
            name="produtos",
            field=models.ManyToManyField(
                related_name="pedidos",
                through="pedido.ItemPedido",
                to="produto.produto",
            ),
        ),
    ]
