# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20170127_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='view',
            new_name='views',
        ),
    ]
