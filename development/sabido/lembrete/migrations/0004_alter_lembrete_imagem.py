# Generated by Django 3.2.13 on 2022-06-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lembrete', '0003_alter_lembrete_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lembrete',
            name='imagem',
            field=models.URLField(max_length=300),
        ),
    ]
