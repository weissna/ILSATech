'''
Created on Mar 7, 2017

@author: weissna
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]