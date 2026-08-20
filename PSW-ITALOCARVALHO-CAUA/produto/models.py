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
    nome = models.CharField(max_length=100, choices=NOME_CHOICES, unique=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome



class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return self.nome


class Flor(models.Model):   
    TAMANHO_CHOICES = [
        ('P', 'Pequena'),
        ('M', 'Média'),
        ('G', 'Grande'),
    ] 
    #Conecta ao modelo Produto
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name='flor')
    tamanho = models.CharField(max_length=1, choices=TAMANHO_CHOICES)

    #Função para determinar o espaço ocupado pela flor com base no tamanho

    @property
    def espaco_ocupado(self):
        espacos ={
            'P': 1,
            'M': 1.5,
            'G': 2,
        }
        
        return espacos[self.tamanho]

    def __str__(self):
        return f'{self.produto.nome} - {self.get_tamanho_display()}'


    #Classe intermediária para guardar a quantidade de cada flor em um arranjo
class ArranjoFlor(models.Model):

    arranjo = models.ForeignKey('Arranjo', on_delete=models.CASCADE)
    flor = models.ForeignKey(Flor, on_delete=models.CASCADE)
    #recebe numeros inteiros positivos
    quantidade = models.PositiveIntegerField(
        default=1,
    )     


class Arranjo(models.Model):
    TAMANHO_CHOICES = [
        ('P', 'Pequena'),
        ('M', 'Média'),
        ('G', 'Grande'),
    ]

        
    #Conecta ao modelo Produto  
      
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name='arranjo')
    tamanho = models.CharField(max_length=1, choices=TAMANHO_CHOICES)
    flores = models.ManyToManyField(Flor,  through='ArranjoFlor', related_name='arranjos', blank=True)


    #Função para determinar a capacidade do arranjo com base no tamanho
    @property
    def capacidade(self):
        capacidades ={
            'P': 12,
            'M': 18,
            'G': 24,
        }

        return capacidades[self.tamanho]
    def __str__(self):
        return f"{self.produto.nome} - {self.get_tamanho_display()}"


#Classe Meta para impedir que a mesma flor seja adicionada mais de uma vez ao mesmo arranjo
class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=['arranjo', 'flor'],
            name='flor_unica_por_arranjo'
        )
    ]    