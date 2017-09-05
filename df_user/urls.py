# -*- coding: utf-8 -*-
# __author__ = 'zhudewei'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/register/$', views.register),
    url(r'^user/register_handle/$', views.register_handle),
    url(r'^user/login/$', views.login),
]
