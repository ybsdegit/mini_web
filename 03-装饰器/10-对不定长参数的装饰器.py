#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 21:53
# @Author  : Paulson
# @File    : 10-对不定长参数的装饰器.py
# @Software: PyCharm
# @define  : function


def set_func(func):
    def call_fun(*args, **kwargs):
        print('----这是权限验证1----')
        print('----这是权限验证2----')
        # func(args, kwargs)  # 不行，相当他传递了2个参数：1个元组，一个字典
        func(*args, **kwargs)  # 拆包
    
    return call_fun


@set_func  # 等价于 test1 = set_func(test1)
def test1(num, *args, **kwargs):
    print(f'----test1----{num}')
    print('----test1----', args)
    print('----test1----', kwargs)


test1(100)
test1(100, 200)
test1(100, 200, 300, mm=100)
