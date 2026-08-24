from django.contrib import admin
from .models import Categoria, Produto, Flor, Arranjo


admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Flor)
admin.site.register(Arranjo)