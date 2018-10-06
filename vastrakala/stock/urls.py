from django.conf.urls import url
from . views import ItemGroupListView,item_stock_list,ItemStockDetailView,\
    checkout,add_item_group,add_item_stock,Customers

from django.conf import settings
from django.conf.urls.static import static

app_name='stock'

urlpatterns = [
    url(r'^$',ItemGroupListView.as_view(),name="index"),
    # url(r'^products/$',ItemStockListView.as_view(),name="products"),
    url(r'^products/(?P<pk>[0-9]+)/$',item_stock_list,name="products"),
    url(r'^products/details/(?P<pk>[0-9]+)/$',ItemStockDetailView.as_view(),name="product-detail"),
    # url(r'^carts/$',view_cart,name="cart"),
    url(r'^checkout/$',checkout,name="checkout"),
    url(r'^accounts/item-group/new/$',add_item_group,name="add_item_group"),
    url(r'^accounts/item-stock/new/$',add_item_stock,name="add_item_stock"),

    # url(r'^getcust/$',Customers.as_view(),name="getcust"),
]+  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)