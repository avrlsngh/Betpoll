# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-20 07:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matches', '0009_auto_20200119_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_side', models.IntegerField(default=None, null=True)),
                ('match', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='matches.Match')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userright',
            name='match_voted',
        ),
    ]