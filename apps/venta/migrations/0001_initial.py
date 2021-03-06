# Generated by Django 3.1.7 on 2021-03-21 21:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150, unique=True, verbose_name='Nombre de la categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=150, unique=True, verbose_name='Nombre del producto')),
                ('apellidos', models.CharField(max_length=150, unique=True, verbose_name='Nombre del producto')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='Numero de identidad')),
                ('fecha_nacimiento', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de nacimiento')),
                ('direccion', models.CharField(max_length=150, verbose_name='Direccion')),
                ('sexo', models.CharField(choices=[('Honbre', 'Hombre'), ('Mujer', 'Mujer')], max_length=50, verbose_name='Sexo')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nombres'],
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de venta')),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Impuesto al valor agregado')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Total venta')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.cliente')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150, unique=True, verbose_name='Nombre del producto')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='product/%y/%m/%d')),
                ('pvp', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio del producto')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad del producto')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Subtotal detalle')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.producto')),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.venta')),
            ],
            options={
                'verbose_name': 'Detalle Venta',
                'verbose_name_plural': 'Detalle Ventas',
                'ordering': ['id'],
            },
        ),
    ]
