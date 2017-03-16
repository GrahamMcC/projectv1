from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #urls for log in and forgot password
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^my_info$', views.my_info, name='my_info'),
    url(r'^internal_admin$', views.admin, name='internal_admin'),
    url(r'^reports$', views.reports, name='reports'),

    #urls for list views
    url(r'^staff_list$', views.staff_list, name='staff_list'),
    url(r'^car$', views.car_list, name='car_list'),
    url(r'^faculty$', views.faculty_list, name='faculty_list'),
    url(r'^school$', views.school_list, name='school_list' ),
    url(r'^journey_list$', views.journey_list, name='journey_list'),

    #urls for detail views
    url(r'^car/(?P<pk>\d+)/$', views.car_detail, name='car_detail'),
    url(r'^journey/(?P<pk>\d+)/$', views.journey_detail, name='journey_detail'),
    url(r'^journey/(?P<pk>\d+)/booked/$', views.journey_booked, name='journey_booked'),


    #urls for new views
    url(r'^car/new/$', views.car_new, name='car_new'),
    url(r'^school/new/$', views.school_new, name='school_new'),
    url(r'^journey/new/$', views.journey_new, name='journey_new'),
    url(r'^faculty/new/$', views.faculty_new, name='faculty_new'),
    url(r'^user/new/$', views.user_new, name ='user_new'),
    url(r'^staff/new/$', views.staff_new, name='staff_new'),

    #urls for edit views
    url(r'^car/(?P<pk>\d+)/edit/$', views.car_edit, name='car_edit'),
    url(r'^school/(?P<pk>\d+)/edit/$', views.school_edit, name='school_edit'),
    url(r'^faculty/(?P<pk>\d+)/edit/$', views.faculty_edit, name='faculty_edit'),
    url(r'^staff/(?P<pk>\d+)/edit/$', views.staff_edit, name='staff_edit'),
    url(r'^journey/(?P<pk>\d+)/edit/$', views.journey_edit, name='journey_edit'),
]
