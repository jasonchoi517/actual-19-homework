# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(db_index=True, max_length=50, unique=True)),
                ('cpu_num', models.IntegerField(db_index=True, verbose_name='cpu核数')),
                ('cpu_model', models.CharField(max_length=100, verbose_name='cpu型号')),
                ('mem_total', models.CharField(default='8G', max_length=3, verbose_name='内存')),
            ],
        ),
    ]