from django.contrib import admin
from .models import Produto, Loja, Venda

# admin.site.register(Task)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass

@admin.register(Loja)
class LojaAdmin(admin.ModelAdmin):
    pass

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ['pk', 'quantidade', 'valor', 'criado_em']