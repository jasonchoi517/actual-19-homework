# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-03 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20181028_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]