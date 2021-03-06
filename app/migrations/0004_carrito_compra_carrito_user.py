# Generated by Django 4.0.4 on 2022-06-28 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_alter_orden_fecha_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='compra',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='carrito',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
