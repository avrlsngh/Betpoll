# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-18 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_userright'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_end_time',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_start_time',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
