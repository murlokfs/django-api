from celery import shared_task
from .models import Venda
import time
import logging

logger = logging.getLogger(__name__)

@shared_task
def atualizar_vendas_pendentes():
    vendas_pendentes = Venda.objects.filter(status='em_andamento')
    contagem_atualizadas = 0
    for venda in vendas_pendentes:
        venda.status = 'concluido'
        venda.save()
        contagem_atualizadas += 1
        print(f"{venda.id} concluida")

    time.sleep(20)
    return f'{contagem_atualizadas} vendas atualizadas para concluídas'

@shared_task
def teste_task():
    print('Tarefa teste executada com sucesso')
    return 'Sucesso'

