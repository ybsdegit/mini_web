#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 22:04
# @Author  : Paulson
# @File    : 08-用同一个装饰器对多个函数进行装饰.py
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
    

@set_func
def test2(num):
    print(f'----test2----{num}')


test1(100)
test2(40)
