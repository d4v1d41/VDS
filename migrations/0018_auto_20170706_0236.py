# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 05:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='texto',
        ),
    ]
