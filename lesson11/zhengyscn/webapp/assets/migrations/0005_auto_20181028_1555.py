# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 07:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20181028_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assets',
            old_name='creat_time',
            new_name='create_time',
        ),
    ]