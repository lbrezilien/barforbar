# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20160229_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='about',
            name='school',
        ),
        migrations.AlterField(
            model_name='about',
            name='why_quote',
            field=models.DateField(),
        ),
    ]
