# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20160229_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='about',
            name='genre_interests',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='about',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='about',
            name='why_quote',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
