# Generated by Django 3.2.13 on 2022-07-17 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lembrete', '0004_alter_lembrete_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lembrete',
            name='arquivo',
        ),
    ]
