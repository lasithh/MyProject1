# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-10 00:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyInvestementsManager', '0034_auto_20180910_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dividend',
            name='type',
        ),
    ]