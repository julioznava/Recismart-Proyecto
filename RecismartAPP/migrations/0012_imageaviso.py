# Generated by Django 4.1.4 on 2022-12-09 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RecismartAPP', '0011_alter_registroaviso_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageAviso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='publicacion')),
                ('aviso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RecismartAPP.registroaviso')),
            ],
        ),
    ]