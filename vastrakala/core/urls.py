from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'core'

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'accounts/register.html'}, name='login'),

]
