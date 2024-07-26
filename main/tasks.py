from datetime import datetime, timedelta
import time

from celery import shared_task

from .models import Venda

@shared_task
def atualizar_vendas_pendentes():
    vendas_pendentes = Venda.objects.filter(status='em_andamento')
    contagem_atualizadas = 0
    for venda in vendas_pendentes:
        criado_em_datetime = datetime.combine(venda.criado_em, datetime.min.time())

        # Caso a venda tenha sido criada no dia anterior, ela expira.
        if datetime.today() >= criado_em_datetime + timedelta(days=1):
            venda.status = 'expirado'
            venda.save()
            contagem_atualizadas += 1
        print(f"Venda ID:{venda.id} expirada.")  # type: ignore

    time.sleep(20)
    return f'{contagem_atualizadas} vendas atualizadas para concluídas'

@shared_task
def alerta_vendas_pendentes():
    vendas_pendentes = Venda.objects.filter(status='em_andamento')
    contagem_pendentes = 0

    # Checa se há vendas com status de 'em_andamento', e procede com a listagem
    if vendas_pendentes:
        print ('- - - Alerta - - -')
        for venda in vendas_pendentes:
            print(f'Venda ID:{venda.id} será expirada em breve.') # type: ignore
            contagem_pendentes += 1
    return f'\n{contagem_pendentes} vendas serão expiradas'

@shared_task
def teste_task():
    print('Tarefa teste executada com sucesso')
    return 'Sucesso'



