# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-01 05:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesorder',
            name='dealer_code',
        ),
        migrations.DeleteModel(
            name='Dealer',
        ),
    ]
