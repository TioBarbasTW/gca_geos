# Generated by Django 5.1.1 on 2024-09-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gacbase', '0003_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestador',
            name='statusPrestador',
            field=models.BooleanField(default=False, verbose_name=['Disponivel', 'Indisponivel']),
        ),
    ]
