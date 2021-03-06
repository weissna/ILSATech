'''
Created on Mar 7, 2017

@author: weissna
'''
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
]