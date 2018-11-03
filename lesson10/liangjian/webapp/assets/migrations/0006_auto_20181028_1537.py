# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20181028_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='chuangjianshijian'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update time'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='status',
            field=models.IntegerField(choices=[(0, 'GUANJI'), (1, 'kaiji')], verbose_name='status 0 | 1'),
        ),
    ]