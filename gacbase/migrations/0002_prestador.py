# Generated by Django 5.1.1 on 2024-09-16 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gacbase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestador',
            fields=[
                ('codPrestador', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('statusPrestador', models.BooleanField(default=False)),
                ('codCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gacbase.cliente')),
            ],
        ),
    ]
