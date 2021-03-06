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
from django.conf.urls import url, include
from django.contrib import admin

from api.views import CommandView, LoginView, LoginPageView
from assets.views import assetsView,deleteAssetsView,addAssetsView,addPageAssetsView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include("api.urls")),
    url(r'^dashboard/', include("dashboard.urls")),
    url(r'^users/', include("users.urls")),
    url(r'^command/', include("command.urls")),
    url(r'^ssum/', include("ssum.urls")),
    url(r'^assets/', assetsView),
    url(r'^assets/addpage/$', addPageAssetsView),
    url(r'^assets/add/$',addAssetsView ),
    url(r'assets/delete/$',deleteAssetsView ),
]
