from django.contrib.auth.models import User
from django.db import models


class Usuario(User):
    cpf = models.CharField(max_length=14)

    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.username
