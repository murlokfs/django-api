# Generated by Django 5.0.6 on 2024-07-16 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_produto_estoque_venda'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='status',
            field=models.CharField(choices=[('em_andamento', 'Em andamento'), ('concluido', 'Concluido'), ('reembolsado', 'Re-embolsado')], default=(), max_length=12),
        ),
    ]
