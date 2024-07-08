from django.contrib import admin
from .models import Produto, Loja

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass

@admin.register(Loja)
class LojaAdmin(admin.ModelAdmin):
    pass
