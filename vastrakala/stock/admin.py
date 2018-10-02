# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from . models import ItemType,ItemGroup,ItemStock
# Register your models here.


class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'slug', 'created_at','updated_at',]
    prepopulated_fields = {'slug': ('type',)}


admin.site.register(ItemType,ItemTypeAdmin)


class ItemGroupAdmin(admin.ModelAdmin):
    list_display = ['group', 'slug', 'price', 'type', 'description','available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'type', 'available','description']
    prepopulated_fields = {'slug': ('group',)}


admin.site.register(ItemGroup,ItemGroupAdmin)


class ItemStockAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_group', 'slug', 'price', 'stock', 'description','available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['item_group','stock','price', 'available','description']
    prepopulated_fields = {'slug': ('item_name',)}


admin.site.register(ItemStock,ItemStockAdmin)