# Generated by Django 2.0.1 on 2018-02-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webbody', '0026_auto_20180219_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juegos',
            name='codigo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='juegos',
            name='sinopsis',
            field=models.CharField(help_text='máximo 9999 caracteres', max_length=9999),
        ),
        migrations.AlterField(
            model_name='juegos',
            name='size',
            field=models.CharField(help_text='maximo 10 caracteres', max_length=10),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='sinopsis',
            field=models.CharField(help_text='máximo 300 caracteres', max_length=9999),
        ),
    ]
