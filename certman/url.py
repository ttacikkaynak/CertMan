#from django.conf.urls import url
from django.urls import include, re_path
from certman import views

urlpatterns = [
    re_path(r'^dashboard/$', views.index, name='dashboard'),
    re_path(r'^user_login/$', views.user_login, name='user_login'),
]