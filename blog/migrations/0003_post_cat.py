# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cat',
            field=models.CharField(choices=[('green', 'green'), ('red', 'red')], max_length=256, null=True),
        ),
    ]