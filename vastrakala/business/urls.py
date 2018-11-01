from django.conf.urls import url
from . import views
from accounts import views as account_views


app_name='business'

urlpatterns = [
    url(r'^$',views.business,name="business"),
    url(r'^blank/$',views.blank,name="blank"),
    # url(r'^order/$',views.create_order,name="create_order"),

    url(r'^customer/$',account_views.show_customers,name="customer"),
    url(r'^customer/(?P<pk>\d+)/$',account_views.show_customers,name="customer"),
    url(r'^delete-customers/$',account_views.delete_customer,name='delete_customer'),

    url(r'^reseller/$',account_views.show_resellers,name="reseller"),
    url(r'^reseller/(?P<pk>\d+)/$',account_views.show_resellers,name="reseller"),
    url(r'^delete-reseller/$',account_views.delete_reseller,name="delete_reseller"),

    url(r'^dealer/$',account_views.show_dealers,name="dealer"),
    url(r'^dealer/(?P<pk>\d+)/$',account_views.show_dealers,name="dealer"),
    url(r'^delete-dealer/$',account_views.delete_dealer,name="delete_dealer"),

    url(r'^order/$', account_views.make_so, name='make_so'),
    url(r'^order/list/$',account_views.SOListView.as_view(), name='orders'),

]