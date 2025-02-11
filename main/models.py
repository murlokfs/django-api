from typing import Any, Iterable

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

# class User(AbstractUser):
#     pass

# class Task(models.Model):

#     STATUSTASK = (
#         ('pendente', 'Pendente'),
#         ('concluido', 'Concluido')
#     )

#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=12,choices=STATUSTASK, default=STATUSTASK[0:0])
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

#     def __str__(self):
#         return self.title

class Loja(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    estoque = models.PositiveIntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Venda(models.Model):
    STATUSCHOICES = (
        ('em_andamento', 'Em andamento'),
        ('concluido', 'Concluido'),
        ('expirado', 'Expirado'),
        ('reembolsado', 'Re-embolsado')
    )

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    criado_em = models.DateField(auto_now_add=True)
    quantidade = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=12, choices=STATUSCHOICES, default=STATUSCHOICES[0:0]) # type: ignore

    def __str__(self):
        return f'ID: {self.pk}'
    
    def save (self, *args, **kwargs):
        if self.quantidade > self.produto.estoque:
            raise ValidationError(f'O produto não possui estoque suficiente. (Estoque: {self.produto.estoque})')
        elif self.status == 'em_andamento':
            self.produto.estoque -= self.quantidade
            self.produto.save()
        elif self.status == 'concluido':
            self.produto.save()
        elif self.status == 'reembolsado':
            self.produto.estoque += self.quantidade
            self.produto.save()

        super(Venda, self).save(*args, **kwargs)