# Core django imports
from django.conf.urls import url

# Imports from app
from . import views

urlpatterns = [url(r'^$', views.home, name='home'),
               url(r'^$', views.input, name='input'),
               url(r'^$', views.list, name='list'),
               url(r'^$', views.first_check, name='first_check'),
               url(r'^$', views.second_check, name='second_check'),
               url(r'^$', views.index_sample, name='results'),
               url(r'^$', views.modify_sample, name='modify'),
               url(r'^$', views.contact, name='contact'),
               url(r'^$', views.request_list, name='request_list'),
               url(r'^$', views.display, name='display'),
#               url(r'^$', views.product_list, name='product_list'),
               url(r'^login/$', 'django.contrib.auth.views.login',
                   name='login',
                   kwargs={'template_name': 'table/login.html'}),
               url(r'^logout/$', 'django.contrib.auth.views.logout',
                   name='logout', kwargs={'next_page': '/'}), ]
