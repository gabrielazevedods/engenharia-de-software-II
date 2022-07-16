# Generated by Django 3.2.13 on 2022-05-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lembrete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=250)),
                ('imagem', models.ImageField(upload_to='lembretes')),
                ('arquivo', models.FileField(upload_to='lembretes')),
            ],
        ),
    ]
