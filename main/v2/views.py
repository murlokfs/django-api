from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from main.models import Produto, Loja
from main.serializers import ProdutoSerializer, LojaSerializer

# -=-=-=-=-=-=-=-=- ViewSets -=-=-=-=-=-=-=-=-

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    # @action(detail=False, methods=['get'])
    # def filter_by_name(self, request):
    #     title = 'Produto'
    #     if title != None:
    #         filtered = self.queryset.filter(nome__icontains=title)
    #         serializer = self.get_serializer(filtered, many=True)
    #         return Response(serializer.data)
    #     else:
    #         return Response({"error":"Titulo requerido"}, status=400)


class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer