from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.staff_list, name='staff_list'),
    url(r'^car$', views.car_list, name='car_list'),
    url(r'^car/(?P<pk>\d+)/$', views.car_detail, name='car_detail'),
    url(r'^car/new/$', views.car_new, name='car_new'),
    url(r'^car/(?P<pk>\d+)/edit/$', views.car_edit, name='car_edit'),
]
