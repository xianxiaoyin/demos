'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 前端模板标签
Date: 2020-12-28 15:49:02
LastEditTime: 2021-02-01 14:27:46
'''
from django.utils.html import format_html
from django import template
register = template.Library()


@register.simple_tag
def circle_page(curr_page, loop_page):
    '''分页'''
    offset = abs(curr_page - loop_page)
    if offset < 3:
        if curr_page == loop_page:
            page_ele = '<li class="active"><a href="?page=%s">%s</a></li>'%(loop_page,loop_page)
        else:
            page_ele = '<li><a href="?page=%s">%s</a></li>'%(loop_page,loop_page)
        return format_html(page_ele)
    return ''
