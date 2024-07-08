from django.urls import path
from .views import *

urlpatterns = [
    path('produtos/', ProdutosAPIView.as_view(), name='produtos'),
    path('produtos/<int:pk>', ProdutoAPIView.as_view(), name='produto'),
    path('lojas', LojasAPIView.as_view(), name='lojas'),
    path('lojas/<int:pk>', LojaAPIView.as_view(), name='loja'),
    # path('lojas/<int:loja_pk>/produtos/', LojasAPIView.as_view(), name='loja-produtos'),
    # path('lojas/<int:loja_pk>/produtos/<int:produto_pk>', LojaAPIView.as_view(), name='loja-produtos-detail'),
]

