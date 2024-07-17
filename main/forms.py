from django import forms
from .models import *

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = '__all__'

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'