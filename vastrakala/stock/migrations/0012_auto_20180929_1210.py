# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-29 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_auto_20180125_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemtype',
            options={'ordering': ('type',)},
        ),
        migrations.AlterField(
            model_name='itemtype',
            name='type',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
