# Generated by Django 5.0.6 on 2024-07-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, default='media/default.png', upload_to='media/'),
        ),
    ]
