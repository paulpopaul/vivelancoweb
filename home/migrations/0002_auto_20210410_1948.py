# Generated by Django 3.0.8 on 2021-04-10 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'ordering': ['Encabezado'], 'verbose_name': 'Pagina de Inicio', 'verbose_name_plural': 'Pagina de Inicio'},
        ),
        migrations.RenameField(
            model_name='home',
            old_name='nombre',
            new_name='Encabezado',
        ),
    ]
