# Generated by Django 4.0.4 on 2022-07-11 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_subscripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=1),
        ),
    ]
