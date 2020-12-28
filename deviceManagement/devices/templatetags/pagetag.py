'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-28 15:49:02
LastEditTime: 2020-12-28 16:51:28
'''
from django.utils.html import format_html
from django import template
register = template.Library()


@register.simple_tag()
def circle_page(curr_page, loop_page):
    print(curr_page)
    print(loop_page)
    offset = abs(curr_page - loop_page)
    print(offset)
    if offset < 3:
        if curr_page == loop_page:
            page_ele = '<li class="active"><a href="?page=%s">%s</a></li>'%(loop_page,loop_page)
        else:
            page_ele = '<li><a href="?page=%s">%s</a></li>'%(loop_page,loop_page)
        return format_html(page_ele)
    else:
        return ''