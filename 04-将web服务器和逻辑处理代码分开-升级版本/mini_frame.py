#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 0:04
# @Author  : Paulson
# @File    : mini_frame.py
# @Software: PyCharm
# @define  : function
import time


def login():
    return f'login Welcome to our website "hahaha" ......{time.ctime()}'


def register():
    return f'register Welcome to our website "hahaha" ......{time.ctime()}'


def profile():
    return f'profile Welcome to our website "hahaha" ......{time.ctime()}'


def application(file_name):
    if file_name == '/login.py':
        return login()
    elif file_name == "/register.py":
        return register()
    else:
        return "Not found you page..."
    