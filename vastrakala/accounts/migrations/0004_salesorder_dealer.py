# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-01 05:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_dealer'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='dealer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.Dealer'),
        ),
    ]