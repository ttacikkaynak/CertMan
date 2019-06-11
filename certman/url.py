from django.conf.urls import url
from certman import views

urlpatterns = [
    url(r'^dashboard/$', views.index, name='dashboard'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]