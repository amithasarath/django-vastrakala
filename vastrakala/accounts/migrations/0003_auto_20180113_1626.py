# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-13 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_dealer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesorder',
            name='client_type',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='reseller',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='type',
        ),
        migrations.DeleteModel(
            name='SalesOrder',
        ),
    ]
