#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 22:01
# @Author  : Paulson
# @File    : 11-对带有返回值的函数进行装饰.py
# @Software: PyCharm
# @define  : function


def set_func(func):
    def call_func(*args, **kwargs):
        print('----这是权限验证1----')
        print('----这是权限验证2----')
        # func(args, kwargs)  # 不行，相当他传递了2个参数：1个元组，一个字典
        return func(*args, **kwargs)  # 拆包
    
    return call_func


@set_func  # 等价于 test1 = set_func(test1)
def test1(num, *args, **kwargs):
    print(f'----test1----{num}')
    print('----test1----', args)
    print('----test1----', kwargs)
    return 'ok'


@set_func
def test2(num):
    return 'p'


ret = test1(100)
print(ret)

ret1 = test2(200)
print(ret1)