# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-09 23:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyInvestementsManager', '0030_auto_20180909_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dividends',
            name='type',
        ),
    ]