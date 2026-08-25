from django import forms

from .models import Pagamento


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = [
            "pedido",
            "formaPagamento",
            "valor",
            "statusPagamento"
        ]

        labels = {
            "pedido": "Pedido",
            "formaPagamento": "Forma de pagamento",
            "valor": "Valor",
            "statusPagamento": "Status",
        }
        widgets = {
            "valor": forms.NumberInput(
                attrs={
                    "step": "0.01"
                }
            )
        }
