# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-29 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0019_auto_20180929_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemstock',
            name='slug',
            field=models.SlugField(default='sssssssss', max_length=100),
            preserve_default=False,
        ),
    ]
