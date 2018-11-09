"""webapp URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from dashboard.views import index
from assets.views import AssetsListView,AssetsDeleteView,AssetsAddView,AssetsExportView,AssetsDetailView,AssetsEditView

from account.views import AccountLoginView, AccountLogoutView




urlpatterns = [
    url(r'^admin/', admin.site.urls),


    # account
    url(r'^account/login/$', AccountLoginView),
    url(r'^account/logout/$', AccountLogoutView),

    # dashboard
    url(r'^$',index),

    #assets
    url(r'^assets/list/$' ,AssetsListView),
    url(r'^assets/add/$' ,AssetsAddView),
    url(r'^assets/export/$', AssetsExportView),
    url(r'^assets/delete/(?P<pk>[0-9]+)/$' ,AssetsDeleteView),
    url(r'^assets/detail/(?P<pk>\d+)/$', AssetsDetailView),
    url(r'^assets/edit/$', AssetsEditView),




]
