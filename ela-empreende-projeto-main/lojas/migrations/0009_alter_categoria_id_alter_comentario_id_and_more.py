# Generated by Django 5.1.2 on 2024-11-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0008_auto_20241115_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
