# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from decimal import Decimal
from django.conf import settings

# Create your models here.

class ClientType(models.Model):
    client_type = models.CharField(max_length=50)

    def __str__(self):
        return self.client_type


class Reseller(models.Model):
    reseller_name = models.CharField(max_length=100)

    def __str__(self):
        return self.reseller_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name


class Dealer(models.Model):
    dealer_name =models.CharField(max_length=100)
    dealer_code =models.CharField(max_length=5,unique=True)

    def __str__(self):
        return self.dealer_code


class SalesOrder(models.Model):
    status = (
        ('P','Pre-Booked'),
        ('B','Booked'),
        ('D','Dispatched'),
        ('R','Delivered'),
        ('C','Cancelled'),
    )
    client_type     = models.ForeignKey(ClientType,on_delete=models.CASCADE)
    reseller        = models.ForeignKey(Reseller,on_delete=models.CASCADE,blank=True,null=True)
    # new_reseller    = models.BooleanField(default=False)
    customer        = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
    # new_customer    = models.BooleanField(default=False)
    type            = models.ForeignKey('stock.ItemType',on_delete=models.CASCADE)
    cost_price      =   models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
    selling_price   =   models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
    # profit          =   models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    dealer    = models.ForeignKey(Dealer,on_delete=models.CASCADE)
    booking_date    =  models.DateField(default=datetime.date.today)
    tracking_id     = models.CharField(max_length=100,blank=True)
    qty            = models.IntegerField(default=1)
    order_status    =models.CharField(max_length=10,choices=status,blank= False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def __int__(self):
        return self.id

    def get_profit(self):
        return (Decimal(self.selling_price) - Decimal(self.cost_price))