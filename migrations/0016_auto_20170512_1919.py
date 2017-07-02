# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_bigc_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bigc',
            name='note',
        ),
        migrations.AlterField(
            model_name='bigc',
            name='image_preview',
            field=models.ImageField(default='img/default.png', help_text='Imagenes deben ser de una resolucion: 600px ancho, 400px de alto. Esto para evitar inconvenientes', upload_to='img'),
        ),
    ]
