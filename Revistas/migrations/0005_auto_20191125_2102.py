# Generated by Django 2.2.6 on 2019-11-26 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Revistas', '0004_usuario_gerencia_revista'),
    ]

    operations = [
        migrations.AddField(
            model_name='edicoes',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='revista',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]