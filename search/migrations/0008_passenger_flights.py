# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20170525_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(to='search.Flight'),
        ),
    ]
