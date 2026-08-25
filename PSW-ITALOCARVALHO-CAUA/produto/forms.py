from django import forms

from .models import Categoria, Produto


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
