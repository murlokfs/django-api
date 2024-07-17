from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from main.models import Produto, Loja
from main.serializers import ProdutoSerializer, LojaSerializer

# ============ API V2 ============

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('atualizado_em')
    serializer_class = ProdutoSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer