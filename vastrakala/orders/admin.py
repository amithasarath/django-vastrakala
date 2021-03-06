# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created',
                    'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ['id', 'order', 'price', 'product', 'quantity']
#     list_filter = ['order']
#     inlines = [OrderItemInline]