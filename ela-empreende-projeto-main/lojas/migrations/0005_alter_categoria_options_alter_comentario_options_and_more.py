# Generated by Django 5.1.3 on 2024-11-13 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0004_auto_20241113_0926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name': 'Comentário', 'verbose_name_plural': 'Comentários'},
        ),
        migrations.AddField(
            model_name='categoria',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comentario',
            name='comentario_resposta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='lojas.comentario'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=models.TextField(help_text='Conteúdo do comentário'),
        ),
    ]
