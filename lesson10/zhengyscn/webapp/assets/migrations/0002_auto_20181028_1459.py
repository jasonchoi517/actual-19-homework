# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='host_status',
            field=models.IntegerField(choices=[(0, '关机'), (1, '运行')], default='', verbose_name='机器的状态0|1'),
        ),
    ]
