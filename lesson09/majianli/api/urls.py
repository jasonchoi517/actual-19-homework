from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^command$', views.CommandView),
    url(r'^login$', views.LoginView),
    url(r'^login_page$', views.LoginPageView),
]
