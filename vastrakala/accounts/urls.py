from django.conf.urls import url
from . import views
from core import views as core_views

app_name = 'accounts'

urlpatterns = [
    url(r'^$',views.showDashboard,name='dashboard'),
    url(r'^dealers/$',views.show_dealers,name='dealers'),
    url(r'^resellers/$',views.show_resellers,name='resellers'),
    url(r'^customers/$',views.show_customers,name='customers'),
    url(r'^my-account/$',core_views.update_profile,name='my_account'),
    url(r'^profile/$',core_views.view_profile,name='profile'),

    url(r'^delete-dealers/$',views.delete_dealer,name='delete_dealer'),
    url(r'^delete-resellers/$',views.delete_reseller,name='delete_reseller'),
    url(r'^delete-customers/$',views.delete_customer,name='delete_customer'),

    url(r'^order/$',views.make_so,name = 'make_so'),
    url(r'^orders/$',views.SOListView.as_view(),name = 'so_list'),
    # url(r'^order/edit/(?P<pk>\d+)/$',views.SalesOrderUpdateView.as_view(),name = 'so_update'),
    url(r'^order/edit/(?P<pk>\d+)/$',views.update_so,name = 'update_so'),
    url(r'^order/detail/(?P<pk>\d+)/$',views.SalesOrderDetailView.as_view(),name = 'so_detail'),
    url(r'^order/delete/(?P<pk>\d+)/$',views.SalesOrderDeleteView.as_view(),name = 'so_delete'),

    url(r'^report/daily-sales/$',views.daily_sales_report,name = 'daily_sales_report'),
    url(r'^report/custom-sales/$',views.custom_sales_report,name = 'custom_sales_report'),

    url(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),

    url(r'^api/so-list/$', views.SalesOrderList.as_view(), name='api_so_list'),

    url(r'^api/dealer-list/$', views.DealerList.as_view(), name='api_dealer_list'),
    url(r'^api/dealer-create/$', views.DealerCreate.as_view(), name='api_dealer_create'),
    url(r'^api/dealer-delete/$', views.DealerDelete.as_view(), name='api_dealer_delete'),
    url(r'^api/dealer/(?P<pk>[a-zA-Z0-9]+)/$', views.DealerUpdate.as_view(), name='api_dealer_update'),

]