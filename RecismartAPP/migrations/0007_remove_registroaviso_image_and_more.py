# Generated by Django 4.1.4 on 2022-12-12 02:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecismartAPP', '0006_alter_registroaviso_fecha_publicacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registroaviso',
            name='image',
        ),
        migrations.AlterField(
            model_name='registroaviso',
            name='Fecha_publicacion',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 2, 41, 11, 239815, tzinfo=datetime.timezone.utc)),
        ),
    ]