from django.conf.urls import url
from . views import business,blank,create_order


app_name='business'

urlpatterns = [
    url(r'^$',business,name="business"),
    url(r'^blank/$',blank,name="blank"),
    url(r'^order/$',create_order,name="create_order"),
]