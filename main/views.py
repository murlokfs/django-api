from rest_framework import generics
from rest_framework import viewsets
from .models import Produto, Loja
from .serializers import ProdutoSerializer, LojaSerializer

class ProdutosAPIView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class LojasAPIView(generics.ListCreateAPIView):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer

class LojaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer