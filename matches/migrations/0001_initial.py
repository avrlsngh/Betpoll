# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-18 18:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(blank=True, default=None, max_length=1500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_name', models.CharField(default=None, max_length=250)),
                ('game', models.CharField(default=None, max_length=250)),
                ('player_1', models.CharField(default=None, max_length=250)),
                ('player_2', models.CharField(default=None, max_length=250)),
                ('match_start_time', models.DateTimeField()),
                ('match_end_time', models.DateTimeField()),
                ('match_day', models.IntegerField(default=None)),
                ('match_coordinators', models.CharField(default=None, max_length=250)),
                ('match_round', models.CharField(default=None, max_length=250)),
                ('match_desc', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='matches.Match'),
        ),
        migrations.AddField(
            model_name='chat',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
