# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expose', '0002_auto_20171103_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='article_media_type',
            field=models.CharField(default='Undefined', max_length=20),
        ),
    ]