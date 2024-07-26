from django.urls import path

from .views import ProdutoCreateView, ProdutoListView, ProdutoUpdateView, ProdutoDeleteView
from .views import VendaListView, VendaCreateView, VendaUpdateView, VendaDeleteView

urlpatterns = [
    path('', ProdutoListView.as_view(), name='list-produto'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='create-produto'),
    path('produtos/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='update-produto'),
    path('produtos/<int:pk>/deletar/', ProdutoDeleteView.as_view(), name='delete-produto'),
    path('vendas/', VendaListView.as_view(), name='list-venda'),
    path('vendas/novo/', VendaCreateView.as_view(), name='create-venda'),
    path('vendas/<int:pk>/editar/', VendaUpdateView.as_view(), name='update-venda'),
    path('vendas/<int:pk>/deletar/', VendaDeleteView.as_view(), name='delete-venda'),
]