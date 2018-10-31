from django.conf.urls import url
from . import views
from accounts import views as account_views


app_name='business'

urlpatterns = [
    url(r'^$',views.business,name="business"),
    url(r'^blank/$',views.blank,name="blank"),
    url(r'^order/$',views.create_order,name="create_order"),

    url(r'^customer/$',account_views.show_customers,name="customer"),
    url(r'^customer/(?P<pk>\d+)/$',account_views.show_customers,name="customer"),
    url(r'^reseller/$',views.create_reseller,name="reseller"),
    url(r'^dealer/$',views.create_dealer,name="dealer"),
]