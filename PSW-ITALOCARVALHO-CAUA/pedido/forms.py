from django import forms

from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            "usuario",
            "bairro",
            "rua",
            "num_casa",
            "cep",
            "dataHora",
            "descricao_pedido",
            "valorTotal"
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
            "dataHora": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local"
                },
                format="%Y-%m-%dT%H:%M"
            ),
            "valorTotal": forms.NumberInput(
                attrs={
                    "step": "0.01"
                }
            )
        }
