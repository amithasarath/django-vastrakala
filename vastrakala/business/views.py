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
