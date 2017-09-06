# -*- coding: utf-8 -*-
# __author__ = 'zhudewei'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/register/$', views.register),
    url(r'^user/register_exist/$', views.register_exist),
    url(r'^user/register_handle/$', views.register_handle),
    url(r'^user/login/$', views.login),
    url(r'^user/login_handle/$', views.login_handle),
]
