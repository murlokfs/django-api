from rest_framework import generics
from rest_framework import viewsets
from main.models import Produto, Loja
from main.serializers import ProdutoSerializer, LojaSerializer

# -=-=-=-=-=-=-=-=- ViewSets -=-=-=-=-=-=-=-=-

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer