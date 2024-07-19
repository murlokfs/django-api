from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import random
from datetime import datetime
from .models import *
from .forms import *

class ProdutoListView(generic.ListView):
    queryset = Produto.objects.all().select_related('loja').order_by('-criado_em') # Queryset otimizada
    # queryset = Produto.objects.all().order_by('-criado_em') # Queryset antiga
    template_name = "produtos.html"
    context_object_name = 'produtos'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # produtos_total = self.get_queryset().all().count() # Requisição antiga de retornar a quantidade total de produtos no banco
        produtos_total = context['paginator'].count # Requisição nova, contando a partir do contexto que já existe, paginator.
        now = datetime.now().strftime("%H:%M:%S")
        context["produtos_total"] = produtos_total
        context["now"] = now
        return context
    
    @method_decorator(cache_page(15)) # Cache aplicado à pagina, renovado a cada 15s
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

class ProdutoCreateView(generic.CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos_form.html"
    success_url = reverse_lazy('list-produto')

    def form_valid(self, ProdutoForm):
        cache.clear()
        return super().form_valid(ProdutoForm)
    

class ProdutoUpdateView(generic.UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos_form.html"
    success_url = reverse_lazy('list-produto')

class ProdutoDeleteView(generic.DeleteView):
    model = Produto
    template_name = "produtos_delete.html"
    success_url = reverse_lazy('list-produto')

# ---------------------------

class VendaListView(generic.ListView):
    queryset = Venda.objects.all().select_related('produto').order_by('-id')
    template_name = "vendas.html"
    context_object_name = "vendas"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_concluidas = sum(venda.valor for venda in self.get_queryset().select_related('produto') if venda.status == 'concluido')
        num_concluidas = Venda.objects.filter(status='concluido').count
        now = datetime.now().strftime("%H:%M:%S")
        context['total_concluidas'] = total_concluidas
        context['num_concluidas'] = num_concluidas
        context["now"] = now
        return context

class VendaCreateView(generic.CreateView):
    model = Venda
    form_class = VendaForm
    template_name = "vendas_form.html"
    success_url = reverse_lazy('list-venda')

class VendaUpdateView(generic.UpdateView):
    model = Venda
    form_class = VendaForm
    template_name = "vendas_form.html"
    success_url = reverse_lazy('list-venda')

class VendaDeleteView(generic.DeleteView):
    model = Venda
    template_name = "vendas_delete.html"
    success_url = reverse_lazy('list-venda')