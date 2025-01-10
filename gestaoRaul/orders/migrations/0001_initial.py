# Generated by Django 5.1.4 on 2025-01-10 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comandas', '0003_comanda_status_alter_productcomanda_product'),
        ('products', '0003_product_cuisine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obs', models.TextField(blank=True, null=True)),
                ('queue', models.DateTimeField(auto_now_add=True)),
                ('preparing', models.DateTimeField(blank=True, null=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('delivered', models.DateTimeField(blank=True, null=True)),
                ('canceled', models.DateTimeField(blank=True, null=True)),
                ('id_comanda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comandas.comanda')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]