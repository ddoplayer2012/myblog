# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     blog_tags
   Description :
   Author :       me
   date：          2019/1/4
-------------------------------------------------
   Change Activity:
                   2019/1/4:
-------------------------------------------------
"""
__author__ = 'me'
from django import template
from ..models import Post
from ..models import Category
register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    #获取最新文章
    newest_article = Post.objects.all ().order_by ( '-created_time' )[:num]
    return newest_article



@register.simple_tag
def archives():
    #按月份归档，如果月份不是标准的yyyy-mm-dd格式必定会报错。因为读取到了None无法在urls里面解析
    query_month = Post.objects.dates('created_time', 'month', order='DESC')

    return query_month

@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()