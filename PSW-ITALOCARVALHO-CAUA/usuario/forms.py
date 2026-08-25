from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario


class CriarUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "cpf",
            "telefone"
        ]

        labels = {
            "username": "Nome de usuário",
            "first_name": "Nome",
            "last_name": "Sobrenome",
            "email": "E-mail",
            "cpf": "CPF",
            "telefone": "Telefone",
        }


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "cpf",
            "telefone"
        ]

        labels = {
            "username": "Nome de usuário",
            "first_name": "Nome",
            "last_name": "Sobrenome",
            "email": "E-mail",
            "cpf": "CPF",
            "telefone": "Telefone",
        }
