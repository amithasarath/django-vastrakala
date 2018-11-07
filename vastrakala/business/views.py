# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def business(request):
    return render(request,'business/dashboard.html')


def blank(request):
    return render(request,'business/blank.html')


def create_order(request):
    return render(request,'business/form_sales_order.html')


def create_customer(request):
    return render(request,'business/customer.html')


def create_reseller(request):
    return render(request,'business/reseller.html')


def create_dealer(request):
    return render(request,'business/dealer.html')


def order_list(request):
    return render(request,'business/order.html')


def show_chart(request):
    import json
    # from django.utils import simplejson
    c ={'a':71,'b':32}
    js_data = json.dumps(c)
    return render(request,'business/chart-chartjs.html',{"my_data": js_data})
