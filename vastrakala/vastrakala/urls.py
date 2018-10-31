"""vastrakala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from core import views as core_views

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url(r'^login/$', auth_views.login,{'template_name':'accounts/register.html'},name='login'),

    url(r'^login/$', core_views.home,name='home'),
    # url(r'^login/$', core_views.signup,name='signup'),


    url(r'^logout/$', auth_views.logout,{'next_page':'/'}, name='logout'),

    url(r'',include('stock.urls')),
    url(r'^core/',include('core.urls')),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^orders/', include('orders.urls')),
    url(r'^shop/',include('shop.urls')),
    url(r'^business/',include('business.urls')),

    # url(r'^accounts/$',   include('django.contrib.auth.urls')),
]+  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = core_views.handler404
handler500 = core_views.handler500