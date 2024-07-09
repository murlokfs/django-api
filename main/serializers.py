from .models import Produto, Loja
from rest_framework import serializers

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = [
            'id',
            'nome'
        ]

class ProdutoSerializer(serializers.ModelSerializer):

    # loja = LojaSerializer(read_only=True)
    # loja = serializers.HyperlinkedRelatedField(read_only=True ,view_name='loja-detail')

    class Meta:
        model = Produto
        fields = [
            'id',
            'nome',
            'descricao',
            'preco',
            'criado_em',
            'atualizado_em',
            'loja',
        ]