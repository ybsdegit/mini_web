#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 0:04
# @Author  : Paulson
# @File    : mini_frame.py
# @Software: PyCharm
# @define  : function


def index():
    with open("./templates/index.html", encoding="utf-8") as f:
        return f.read()


def center():
    with open("./templates/center.html", encoding="utf-8") as f:
        return f.read()


# 将函数映射为一个字典
URL_FUNC_DICT = {
    "/index.py": index,
    "/center.py": center,
}


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    
    file_name = env['PATH_INFO']
    # file_name = "/index.py"
    
    """
    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return 'Hello World! 我爱你中国....'
    """
    func = URL_FUNC_DICT[file_name]
    return func()
