#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 21:38
# @Author  : Paulson
# @File    : 装饰器演示.py
# @Software: PyCharm
# @define  : function


def set_func(func):
    def call_fun():
        print('----这是权限验证1----')
        print('----这是权限验证2----')
        func()
    return call_fun


@set_func  # 等价于 test1 = set_func(test1)
def test1():
    print('----test1----')

test1()
test1()
