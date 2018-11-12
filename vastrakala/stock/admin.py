# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from . models import ItemType,ItemGroup,ItemStock
# Register your models here.


class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ['id','type', 'slug', 'created_at','updated_at',]
    prepopulated_fields = {'slug': ('type',)}


admin.site.register(ItemType,ItemTypeAdmin)


class ItemGroupAdmin(admin.ModelAdmin):
    list_display = ['id','group', 'slug','group_image' ,'price', 'type', 'description','available', 'created_at', 'updated_at']
    list_filter = ['type','available', 'created_at', 'updated_at']
    list_editable = ['price', 'type','group_image', 'available','description']
    prepopulated_fields = {'slug': ('group',)}


admin.site.register(ItemGroup,ItemGroupAdmin)


class ItemStockAdmin(admin.ModelAdmin):
    list_display = ['id','item_name','item_group','item_image', 'slug', 'price', 'stock', 'description','available', 'created_at', 'updated_at']
    list_filter = ['item_group','available', 'created_at', 'updated_at']
    list_editable = ['item_group','item_image','stock','price', 'available','description']
    prepopulated_fields = {'slug': ('item_name',)}


admin.site.register(ItemStock,ItemStockAdmin)