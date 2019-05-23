#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 21:48
# @Author  : Paulson
# @File    : 07-对有参数、无返回值的函数进行装饰.py
# @Software: PyCharm
# @define  : function


def set_func(func):
    def call_fun(a):
        print('----这是权限验证1----')
        print('----这是权限验证2----')
        func(a)
    return call_fun


@set_func  # 等价于 test1 = set_func(test1)
def test1(num):
    print(f'----test1----{num}')


test1(100)
