# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_name', models.CharField(max_length=200)),
                ('airport_code', models.CharField(max_length=200)),
            ],
        ),
    ]