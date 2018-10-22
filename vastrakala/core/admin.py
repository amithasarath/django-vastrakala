# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','bio','location','birth_date']
    list_filter = ['user','bio','location','birth_date']
    list_editable = ['bio','location','birth_date']
    # prepopulated_fields = {'slug': ('group',)}
# Register your models here.
admin.site.register(Profile,ProfileAdmin)