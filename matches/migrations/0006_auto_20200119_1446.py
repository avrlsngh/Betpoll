# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-19 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0005_auto_20200118_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_day',
            field=models.CharField(choices=[(b'2020-01-22', b'2020-01-22'), (b'2020-01-23', b'2020-01-23'), (b'2020-01-24', b'2020-01-24')], default=b'2020-01-22', max_length=50),
        ),
    ]
