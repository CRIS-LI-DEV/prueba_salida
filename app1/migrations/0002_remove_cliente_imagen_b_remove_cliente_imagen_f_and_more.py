# Generated by Django 4.2.3 on 2023-07-11 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='imagen_b',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='imagen_f',
        ),
        migrations.RemoveField(
            model_name='productor',
            name='imagen_b',
        ),
        migrations.RemoveField(
            model_name='productor',
            name='imagen_f',
        ),
        migrations.RemoveField(
            model_name='usuariostaff',
            name='imagen_b',
        ),
        migrations.RemoveField(
            model_name='usuariostaff',
            name='imagen_f',
        ),
    ]