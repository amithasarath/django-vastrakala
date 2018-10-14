from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'cart'

urlpatterns = [
    url(r'^my$', views.cart_detail1, name='cart_detail1'),
    url(r'^add1/(?P<product_id>\d+)/$', views.cart_add1, name='cart_add1'),
    url(r'^remove1/(?P<product_id>\d+)/$', views.cart_remove1, name='cart_remove1'),

    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),

    url(r'^checkout/$', auth_views.login,
        {'template_name': 'cart/checkout.html'}, name='checkout'),
    # url(r'^checkout/$', views.checkout, name="checkout"),

]