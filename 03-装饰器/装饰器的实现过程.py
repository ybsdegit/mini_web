#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 21:25
# @Author  : Paulson
# @File    : 装饰器的实现过程.py
# @Software: PyCharm
# @define  : function


def set_func(func):
    def call_fun():
        print('----这是权限验证1----')
        print('----这是权限验证2----')
        func()
    return call_fun


def test1():
    print('----test1----')
    
    
test1 = set_func(test1)

test1()
test1()