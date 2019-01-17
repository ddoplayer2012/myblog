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
from ..models import Category,Tag
from django.db.models.aggregates import Count

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

# @register.simple_tag
# def get_categories():
#     # 别忘了在顶部引入 Category 类
#     return Category.objects.all()


@register.simple_tag
def get_categories():
    #右侧分类总数统计
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称，并且可以过滤
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    # 标签云 统计总数
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


