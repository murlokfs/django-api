from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.apps import apps
from redis import Redis
import time
from django.conf import settings

# Define o módulo de configuração padrão do Django para 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core',broker=settings.CELERY_BROKER_URL)

# Carrega as configurações do projeto Django no Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-detecta tasks dos aplicativos instalados
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'atualizar_vendas_pendentes': {
        'task': 'main.tasks.atualizar_vendas_pendentes',
        'schedule': 60*15, # 15min
    },
    'alerta_vendas_pendentes': {
        'task': 'main.tasks.alerta_vendas_pendentes',
        'schedule': 60*14, # 14min
    },
}

@app.task(bind=True)
def debug_task():
    try:
        Redis(host='localhost', port=6379).ping()
        print("Conexão com Redis bem-sucedida")
    except Exception as e:
        print(f"Erro ao conectar ao Redis: {e}")

if __name__ == '__main__':
    app.start()
