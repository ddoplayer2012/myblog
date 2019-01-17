# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :       me
   date：          2018/12/27
-------------------------------------------------
   Change Activity:
                   2018/12/27:
-------------------------------------------------
"""
__author__ = 'me'


from . import views
from django.conf.urls import url, include
from blog.feeds import AllPostsRssFeed

'''
首页视图匹配的 URL 去掉域名后其实就是一个空的字符串。对文章详情视图而言，每篇文章对应着不同的 URL。比如我们可以把文章详情页面对应的视图设计成这个样子：当用户访问 <网站域名>/post/1/ 时，显示的是第一篇文章的内容，而当用户访问 <网站域名>/post/2/ 时，显示的是第二篇文章的内容，这里数字代表了第几篇文章，也就是数据库中 Post 记录的 id 值。下面依照这个规则来绑定 URL 和视图：
'''
#告诉 Django 这个 urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间。
app_name = 'blog'

urlpatterns = [
   # url(r'^index/', views.IndexView.as_view()),
    url ( r'^all/rss/$', AllPostsRssFeed (), name='rss' ),
    url ( r'^$', views.IndexView.as_view(), name='index' ),
    url ( r'^post/(?P<pk>[0-9]+)/$', views.GetdetailView.as_view(), name='detail' ),
    #(?P<name> 正则匹配规则)为正则命名，然后name作为参数变量名，值作为参数的值匹配到的值传入views里面
    url ( r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives' ),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url ( r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view (), name='tag' ),
]



