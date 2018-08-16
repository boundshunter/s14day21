#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'


from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.simple_tag
def simple_1(arg1, arg2):
    return arg1 + arg2


@register.filter()
def simple_2(arg1, arg2):
    return arg1 + arg2



