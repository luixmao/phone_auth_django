from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^first_page_phone/$', views.first_page_phone, name='first_page_phone'),



    url(r'^check_number/(?P<country_code>[0-9]+)/(?P<numb>[0-9]+)/$',  views.check_number, name='check_number'),

    url(r'^verification_page/(?P<phone_num>[0-9]+)/$',  views.verification_page, name='verification_page'),

    url(r'^check_verification/(?P<numb>[0-9]+)/(?P<code>[0-9]+)/$',  views.verify_code, name='verify_code'),



    url(r'^login/(?P<numb>[0-9]+)/$', views.login, name='login'),

    url(r'^login/auth_view/$', views.auth_view, name='auth_view'),

    url(r'^register/(?P<numb>[0-9]+)/$', views.register, name='register'),
    
    url(r'^logout/$', views.logout, name='logout'),

]