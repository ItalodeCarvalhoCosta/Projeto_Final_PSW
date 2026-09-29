from django import forms
from produto.models import Produto
from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            "bairro",
            "rua",
            "num_casa",
            "cep",
        ]

        labels = {
            "usuario": "Usuário",
            "bairro": "Bairro",
            "rua": "Rua",
            "num_casa": "Número da casa",
            "cep": "CEP",
            "dataHora": "Data e hora",
            "descricao_pedido": "Descrição",
            "valorTotal": "Valor total",
        }
        widgets = {
            
            "valorTotal": forms.NumberInput(
                attrs={
                    "step": "0.01"
                }
            )
        }

class ItemPedidoForm(forms.Form):

    produto = forms.ModelChoiceField(
        queryset=Produto.objects.all()
    )

    quantidade = forms.IntegerField(
        min_value=1,
        initial=1
    )