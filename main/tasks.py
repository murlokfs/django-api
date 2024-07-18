from celery import Celery
from .models import Venda
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

app = Celery('main')

@app.task
def atualizar_vendas_pendentes():
    try:
        vendas_pendentes = Venda.objects.filter(status='em_andamento')
        contagem_atualizadas = 0
        for venda in vendas_pendentes:
            venda.status = 'concluido'
            venda.save()
            contagem_atualizadas += 1
            logger.info(f"{venda.id} concluida")
    except:
        logger.info(f"Erro")
    return f'{contagem_atualizadas} vendas atualizadas para concluídas'
