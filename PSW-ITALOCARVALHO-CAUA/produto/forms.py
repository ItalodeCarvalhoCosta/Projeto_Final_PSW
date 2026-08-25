from django import forms
from .models import Categoria, Produto


class CategoriaForm(forms.ModelForm):

    class Meta:

        model = Categoria

        fields = [
            "nome_categoria",
            "descricao_categoria"
        ]

        labels = {
            "nome_categoria": "Nome",
            "descricao_categoria": "Descrição"
        }



class ProdutoForm(forms.ModelForm):

    class Meta:

        model = Produto

        fields = [
            "categoria",
            "nome_produto",
            "descricao_produto",
            "precoUnitario",
            "quantidadeEstoque",
            "peso",
        ]

        labels = {
            "categoria": "Categoria",
            "nome_produto": "Nome",
            "descricaoproduto": "Descrição",
            "precoUnitario": "Preço (uni)",
            "quantidadeEstoque": "Estoque",
            "peso": "Peso",
        }

        widgets = {

            "precoUnitario": forms.NumberInput(
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