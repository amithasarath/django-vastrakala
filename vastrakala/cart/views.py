# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from stock.models import ItemStock
from .cart import Cart
from .forms import CartAddProductForm
from .forms import CartAddStockForm


@require_POST
def cart_add1(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail1')


def cart_remove1(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail1')


def cart_detail1(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


######################################################################################

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ItemStock, id=product_id)
    form = CartAddStockForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddStockForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/cart.html', {'cart': cart})


def cart_remove(request, product_id):
    print(product_id)
    cart = Cart(request)
    product = get_object_or_404(ItemStock, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def checkout(request):
    return render(request, 'cart/checkout.html')

from django.contrib.auth import views as auth_views

def checkout_login(request):
    # ... logic for logging in ...
    return render(request, 'cart / checkout.html', auth_views.login)