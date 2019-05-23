#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 22:11
# @Author  : Paulson
# @File    : 12-多个装饰器对同一个函数进行装饰.py
# @Software: PyCharm
# @define  : function


def add_qx(func):
    print('----开始进行装饰权限1个功能----')
    
    def call_func(*args, **kwargs):
        print("---这是权限验证1---")
        return func(*args, **kwargs)  # 拆包
    return call_func


def add_xx(func):
    print('----开始进行装饰xxx个功能----')
    
    def call_func(*args, **kwargs):
        print("---这是xxx的功能")
        return func(*args, **kwargs)  # 拆包
    return call_func


@add_qx
@add_xx
def test1():
    print('----test1----')
    
    
test1()
