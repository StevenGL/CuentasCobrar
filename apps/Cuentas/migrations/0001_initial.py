# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asientos_Contables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=2000)),
                ('Tipo_Movimiento', models.CharField(max_length=2)),
                ('Cuenta', models.IntegerField()),
                ('Fecha', models.DateField()),
                ('Monto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Estado', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Cedula', models.CharField(max_length=13)),
                ('Limite_Credito', models.IntegerField()),
                ('Estado', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Tipos_Documentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=2000)),
                ('Cuenta_Contable', models.IntegerField()),
                ('Estado', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=2000)),
                ('Tipo_Movimiento', models.CharField(max_length=2)),
                ('Numero_Documento', models.IntegerField()),
                ('Fecha', models.DateField()),
                ('Monto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('TipoDocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cuentas.Tipos_Documentos')),
            ],
        ),
        migrations.AddField(
            model_name='asientos_contables',
            name='Cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cuentas.Clientes'),
        ),
    ]