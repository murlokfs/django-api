from .models import Produto, Loja
from rest_framework import serializers

# class TaskSerializer(serializers.ModelSerializer):
#     is_completed = serializers.ReadOnlyField()
#     time_to_complete = serializers.ReadOnlyField()

#     class Meta:
#         model = Task
#         fields = [
#             'id', 'title', 'description', 'created_at', 'updated_at', 'completed_at', 'user', 'status'
#             ]


class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = [
            'id',
            'nome'
        ]

class ProdutoSerializer(serializers.ModelSerializer):

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