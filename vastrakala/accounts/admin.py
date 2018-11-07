# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . models import  ClientType, Reseller,Customer,Dealer,SalesOrder


class ClientTypeAdmin(admin.ModelAdmin):
    list_display = ['id','client_type']
    # list_filter = ['item_group','available', 'created_at', 'updated_at']
    list_editable = ['client_type']
    # prepopulated_fields = {'slug': ('item_name',)}

admin.site.register(ClientType, ClientTypeAdmin)


class ResellerAdmin(admin.ModelAdmin):
    list_display = ['id','reseller_name']
    list_editable = ['reseller_name']


admin.site.register(Reseller, ResellerAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','customer_name']
    list_editable = ['customer_name']


admin.site.register(Customer, CustomerAdmin)


class DealerAdmin(admin.ModelAdmin):
    list_display = ['id','dealer_code','dealer_name']
    list_editable = ['dealer_code','dealer_name']

admin.site.register(Dealer, DealerAdmin)


class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ['id','booking_date','order_status','client_type','reseller','customer','type','cost_price','selling_price','qty','created','modified']
    list_editable = ['booking_date','order_status','client_type','reseller','customer','type','cost_price','selling_price','qty']
    list_filter = ['booking_date','order_status','client_type','reseller','customer','type']


admin.site.register(SalesOrder, SalesOrderAdmin)
