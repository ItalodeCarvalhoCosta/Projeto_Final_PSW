from django import forms

from .models import Categoria, Produto, Flor, Arranjo, ArranjoFlor


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            "nome",
            "descricao"
        ]

        labels = {
            "nome": "Nome",
            "descricao": "Descrição"
        }


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "categoria",
            "nome",
            "descricao",
            "preco",
            "estoque",
            "peso",
            "imagem"
        ]

        labels = {
            "categoria": "Categoria",
            "nome": "Nome",
            "descricao": "Descrição",
            "preco": "Preço",
            "estoque": "Estoque",
            "peso": "Peso",
            "imagem": "Imagem",
        }
        widgets = {
            "preco": forms.NumberInput(
                attrs={
                    "step": "0.01"
                }
            ),
            "peso": forms.NumberInput(
                attrs={
                    "step": "0.01"
                }
            )
        }


class FlorForm(forms.ModelForm):
    class Meta:
        model = Flor

        fields =[
            "tamanho"
            ]

        labels = {
            "tamanho": "Tamanho da flor"
        }
class ArranjoForm(forms.ModelForm):
    class Meta:
        model = Arranjo

        fields =[
            "tamanho"
            ]

        labels = {
            "tamanho": "Tamanho do arranjo"
        }

class ArranjoFlorForm(forms.ModelForm):

    class Meta:
        model = ArranjoFlor

        fields = [
            "flor"
            "quantidade"
        ]

        labels = {
            "flor": "Flor",
            "quantidade": "Quantidade"
        }