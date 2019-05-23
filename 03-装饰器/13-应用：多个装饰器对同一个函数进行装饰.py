#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 22:11
# @Author  : Paulson
# @File    : 12-多个装饰器对同一个函数进行装饰.py
# @Software: PyCharm
# @define  : function


def set_func_1(func):
    def call_func():
        return "<h1>" + func() + "</h2>"
    return call_func


def set_func_2(func):
    def call_func():
        return "<td>" + func() + "</td>"
    return call_func


@set_func_1  # 先执行第一个装饰器
@set_func_2
def get_str():
    return "haha"


print(get_str())