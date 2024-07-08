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

    def get_queryset(self):
        if self.kwargs.get('produto_pk'):
            return self.queryset.filter(produto_id = self.kwargs.get('produto_pk'))
        return self.queryset.all()

class LojaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer