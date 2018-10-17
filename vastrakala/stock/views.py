# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from . models import ItemGroup,ItemStock
from . forms import ItemGroupForm,ItemStockForm
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

from cart.forms import CartAddStockForm


class ItemGroupListView(generic.ListView):
    template_name = 'stock/index.html'
    model = ItemGroup

    # def get_queryset(self):
    #     return ItemGroup.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ItemGroupListView,self).get_context_data(**kwargs)
        sarees = ItemGroup.objects.all().filter(type=2)
        churidars = ItemGroup.objects.all().filter(type=1)
        jewels = ItemGroup.objects.all().filter(type=3)

        context["saree_list"]       = sarees
        context["churidar_list"]    = churidars
        context["jewel_list"]       = jewels

        # context.update({
        #     'saree_list': sarees,
        #     'churidar_list': churidars,
        #     'jewel_list': jewels,
        # })
        # print jewels
        return context


class ItemStockListView(generic.ListView):
    template_name = 'stock/products.html'

    def get_queryset(self):
        return ItemStock.objects.all()


from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def item_stock_list(request,pk):

    if pk == "0":
        item_list = ItemStock.objects.all()
    else:
        # item_list = ItemStock.objects.filter(item_group__type = pk)
        item_list = ItemStock.objects.filter(item_group = pk)

    # paginator = Paginator(item_list, 3)  # Show 25 contacts per page
    # page = request.GET.get('page')
    # stocks = paginator.get_page(page)

    page = request.GET.get('page', 1)
    print "------------"
    print page

    paginator = Paginator(item_list, 6)
    print paginator
    print paginator.count
    print paginator.num_pages
    try:
        stocks = paginator.page(page)
    except PageNotAnInteger:
        stocks = paginator.page(1)
    except EmptyPage:
        stocks = paginator.page(paginator.num_pages)
    return render(request,'stock/products.html',{
                                "item_list":stocks,
                                "group_id":pk,
                                "item_groups":ItemGroup.objects.all()
        })


class ItemStockDetailView(generic.DetailView):
    model = ItemStock
    template_name = 'stock/product_detail.html'

    def get_context_data(self, **kwargs):
        # xxx will be available in the template as the related objects
        context = super(ItemStockDetailView, self).get_context_data(**kwargs)
        cart_stock_form = CartAddStockForm()
        context['related_items'] = ItemStock.objects.all()
        # context['related_items'] = ItemStock.objects.filter(item_group=2)
        context['item_groups'] = ItemGroup.objects.all()
        context['cart_stock_form'] = cart_stock_form

        # context[]
        # print self.get_object().item_group
        # print ItemStock.objects.filter(item_group = self.get_object().item_group)
        # print "**********"
        return context


# def view_cart(request):
#     return render(request,'stock/cart.html')


def add_item_group(request):
    if request.method == "POST":
        form = ItemGroupForm(request.POST,request.FILES)
        if form.is_valid():
            # new_group = ItemGroup(data = request.POST)
            # new_group.save()
            form.save()
            return HttpResponseRedirect(reverse('stock:add_item_group'))
        else:
            print (form.errors)
    else:
        form = ItemGroupForm()
        return render(request,'stock/add_item_group.html',{'form':form})


def add_item_stock(request):
    if request.method == "POST":
        form = ItemStockForm(request.POST,request.FILES)
        if form.is_valid():
            # new_group = ItemGroup(data = request.POST)
            # new_group.save()
            form.save()
            return HttpResponseRedirect(reverse('stock:add_item_stock'))
        else:
            print (form.errors)
    else:
        form = ItemStockForm
        return render(request,'stock/add_item_stock.html',{'form':form})

from django.views.generic import TemplateView

class Customers(TemplateView):
    def getCust(request):
        name='liran'
        return HttpResponse('{ "name":"' + name + '", "age":31, "city":"New York" }')
