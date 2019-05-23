#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 0:04
# @Author  : Paulson
# @File    : mini_frame.py
# @Software: PyCharm
# @define  : function 用装饰器自动生成字典
# 将函数映射为一个字典

"""
URL_FUNC_DICT = {
    "/index.html": index,
    "/center.html": center,
}
"""
import re
import pymysql

URL_FUNC_DICT = dict()


def route(url):                              # url = "./index.py"
    def set_func(func):                      # func = index函数的引用
        URL_FUNC_DICT[url] = func  # URL_FUNC_DICT[url = "./index.py"] = index
        
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route("/index.html")       # 请求: 127.0.0.1:7890/index.py
def index():
    with open("./templates/index.html", encoding="utf-8") as f:
        content = f.read()
    
    # my_stock_info = "哈哈哈哈，这是你的本月名称...."
    # content = re.sub(r"\{%content%\}", my_stock_info, content)
    
    # 创建 Connction 对象
    db = pymysql.connect(host='localhost', port=3306, user='root', password='mima',
                         database='stock_db', charset='utf8')
    # 获得 Cursot 对象
    cursor = db.cursor()
    
    sql = """select * from info;"""
    cursor.execute(sql)
    data_from_mysql = cursor.fetchall()  # 元组
    cursor.close()
    db.close()
    
    tr_template = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
                </td>
            </tr>
    """
    html = ""
    for line_info in data_from_mysql:
        html += tr_template % (line_info[0], line_info[1], line_info[2],
                               line_info[3], line_info[4], line_info[5],
                               line_info[6], line_info[7])
    
    # content = re.sub(r"\{%content%\}", str(tr_template), content)
    content = re.sub(r"\{%content%\}", html, content)
    return content
        

@route("/center.html")
def center():
    with open("./templates/center.html", encoding="utf-8") as f:
        content = f.read()

        # 创建 Connction 对象
        db = pymysql.connect(host='localhost', port=3306, user='root', password='mima',
                             database='stock_db', charset='utf8')
        # 获得 Cursot 对象
        cursor = db.cursor()

        sql = """select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info from info as i inner join focus as f on i.id=f.info_id;"""
        cursor.execute(sql)
        data_from_mysql = cursor.fetchall()  # 元组
        print(str(data_from_mysql))
        cursor.close()
        db.close()

        html_template = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <a type="button" class="btn btn-default btn-xs"
                    href="/update/111.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                </td>
                <td>
                    <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="1666">
                </td>
            </tr>
        """
        html = ""
        for line_info in data_from_mysql:
            html += html_template % (line_info[0], line_info[1], line_info[2],
                                     line_info[3], line_info[4], line_info[5], line_info[6])
       
        # print(html)
        content = re.sub(r"\{%content%\}", html, content)
        # print(content)
        return content


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
    # if file_name in URL_FUNC_DICT:
    try:
        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return f"产生了异常:{str(ret)}"
