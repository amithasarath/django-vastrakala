# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from . models import ItemType,ItemGroup
# Register your models here.

admin.site.register(ItemType)
admin.site.register(ItemGroup)