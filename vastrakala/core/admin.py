# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . models import Profile,Address

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','bio','location','birth_date']
    list_filter = ['user','bio','location','birth_date']
    list_editable = ['bio','location','birth_date']
    # prepopulated_fields = {'slug': ('group',)}


admin.site.register(Profile,ProfileAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','house_no','city','landmark','district','state','country','pincode','mobile_number']
    list_filter = ['user','house_no','city','landmark','district','state','country','pincode','mobile_number']
    list_editable = ['house_no','city','landmark','district','state','country','pincode','mobile_number']
    # prepopulated_fields = {'slug': ('group',)}


admin.site.register(Address,AddressAdmin)
