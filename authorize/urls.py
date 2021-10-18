# coding=utf-8
from django.conf.urls import url
from django.contrib import messages
from django.shortcuts import render

from . import views

urlpatterns = [
    url(r'^$', views.showAuth),
    url(r'^login_auth', views.login_site, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^login_site', views.login_site, name='login'),
    url(r'^logout', views.logout_site, name='logout'),
    url(r'^toast', views.authToast),
]

