# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .models import Produto, Cliente
from .serializers import ProdutoSerializer, ClienteSerializer

# class ProdutoListCreateAPIView(ListCreateAPIView):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer

# class ProdutoDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer