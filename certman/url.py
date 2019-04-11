from django.conf.urls import url
from certman import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.dashboard, name='dashboard'),

]