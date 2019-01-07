# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     forms
   Description :
   Author :       me
   date：          2019/1/7
-------------------------------------------------
   Change Activity:
                   2019/1/7:
-------------------------------------------------
"""
__author__ = 'me'

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']