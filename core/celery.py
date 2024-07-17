from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define o módulo de configuração padrão do Django para 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Carrega as configurações do projeto Django no Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-detecta tasks dos aplicativos instalados
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'atualizar_vendas_pendentes': {
        'task': 'main.tasks.atualizar_vendas_pendentes',
        'schedule': 30,  
    },
}