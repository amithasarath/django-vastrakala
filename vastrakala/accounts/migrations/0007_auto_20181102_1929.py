# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-02 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20181102_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer'),
        ),
    ]
