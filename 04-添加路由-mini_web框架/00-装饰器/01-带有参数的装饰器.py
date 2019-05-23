#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 23:01
# @Author  : Paulson
# @File    : 01-带有参数的装饰器.py
# @Software: PyCharm
# @define  : function


def set_func(func):
    
    def call_func(*args, **kwargs):
        level = args[0]
        if level == 1:
            print('----权限级别1验证----')
        elif level == 2:
            print('----权限级别2验证----')
            
        return func()
    return call_func


@set_func
def test1():
    print('---test1---')
    return "ok"


@set_func
def test2():
    print("----test2----")
    return "ok"


test1(1)
test2(2)

