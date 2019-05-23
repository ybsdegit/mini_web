#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 23:26
# @Author  : Paulson
# @File    : 02-带有参数的装饰器2.py.py
# @Software: PyCharm
# @define  : function


def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print('----权限级别1验证----')
            elif level_num == 2:
                print('----权限级别2验证----')
            return func()
        return call_func
    return set_func


# 1 调用 set_func 并且将 1 当做实参 传递
# 2 用上一步调用的返回值 当做 装饰器对test1函数进行装饰

@set_level(1)
def test1():
    print('---test1---')
    return "ok"


@set_level(2)
def test2():
    print("----test2----")
    return "ok"


test1()
test2()
