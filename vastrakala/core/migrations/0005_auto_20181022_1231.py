# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-10-22 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20181022_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresses',
            name='mobile_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='pincode',
            field=models.IntegerField(blank=True),
        ),
    ]
