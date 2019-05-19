#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 0:04
# @Author  : Paulson
# @File    : mini_frame.py
# @Software: PyCharm
# @define  : function


def index():
    return '这是主页'


def login():
    return '这是登录页'


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    
    file_name = environ['PATH_INFO']
    
    if file_name == "/index.py":
        return index()
    elif file_name == '/login.py':
        return login()
    else:
        return 'Hello World! 我爱你中国'
