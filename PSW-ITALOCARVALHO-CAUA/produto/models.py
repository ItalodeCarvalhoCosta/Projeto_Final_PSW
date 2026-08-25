from django.db import models
from decimal import Decimal
from django.core.exceptions import ValidationError

# Create your models here.

class Categoria(models.Model):
    NOME_CHOICES = [
        ('flores', 'Flores'),
        ('arranjos', 'Arranjos'),
        ('mudas', 'Mudas'),
        ('ferramentas', 'Ferramentas'),
        ('outros', 'Outros'),
    ]
    nome_categoria = models.CharField(max_length=100, choices=NOME_CHOICES, unique=True)
    descricao_categoria = models.TextField()

    def __str__(self):
        return self.nome_categoria



class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    nome_produto = models.CharField(max_length=100)
    descricao_produto = models.TextField()
    precoUnitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidadeEstoque = models.IntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome_produto




  