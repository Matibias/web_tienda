# Generated by Django 4.0.4 on 2022-06-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_producto_cantidad_carrito_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='fecha_compra',
            field=models.DateTimeField(),
        ),
    ]