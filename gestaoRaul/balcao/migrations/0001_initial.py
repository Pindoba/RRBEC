# Generated by Django 5.1.4 on 2024-12-10 01:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('mesas', '0001_initial'),
        ('typePay', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dt_open', models.DateTimeField(auto_now_add=True)),
                ('dt_close', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.client')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mesas.mesa')),
                ('type_pay', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='typePay.typepay')),
            ],
        ),
    ]