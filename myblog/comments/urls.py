# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :       me
   date：          2019/1/7
-------------------------------------------------
   Change Activity:
                   2019/1/7:
-------------------------------------------------
"""
__author__ = 'me'

from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]