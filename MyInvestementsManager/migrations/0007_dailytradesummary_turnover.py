# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyInvestementsManager', '0006_auto_20160826_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailytradesummary',
            name='turnover',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
