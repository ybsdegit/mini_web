#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 22:32
# @Author  : Paulson
# @File    : 01-面向对象-多进程实现http服务器_WSGI.py
# @Software: PyCharm
# @define  : function

import re
import socket
import multiprocessing  # 多进程
# import time
import sys
# from dynamic import mini_frame


class WSGIServer(object):
    def __init__(self, port, app):
        #  1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置当服务器先close ，即服务器4次挥手之后资源能够立即释放，这样就保证了，下次运s行程序时，可以立即访问
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
        #  2. 绑定
        self.tcp_server_socket.bind(("", port))
    
        #  3. 监听套接字
        self.tcp_server_socket.listen(128)
        
        self.application = app
    
    def service_client(self, new_socket):
        """
         为这个客户 端返回数据
        :param new_socket:
        :return:
        """
        # 1. 接收浏览器发送过来的请求，即http请求
        # Get / HTTP/1.1
        request = new_socket.recv(1024).decode('utf-8')
        # print(request)
        
        request_lines = request.splitlines()
        print("")
        print(">" * 20)
        print(request_lines)
        
        file_name = ''
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
            print("*" * 50, file_name)
            if file_name == '/':
                file_name = '/index.html'

        # 2. 返回http格式的数据给浏览器
        # 2.1 如果请求的资源不是以 .py 结尾，那么就认为是静态资源（html/css/js/png/jpg等）
        if not file_name.endswith(".py"):
        
            try:
                f = open("./static" + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "-----file not found---"
                new_socket.send(response.encode('utf-8'))
            else:
                html_content = f.read()
                f.close()
                # 2.1 准备发送给浏览器的数据---header
                response = "HTTP/1.1 200 OK\r\n"
                response += '\r\n'
                # 2.2 准备发送给浏览器的数据---body
                # 将response header 发送给浏览器
                new_socket.send(response.encode('utf-8'))
                # 讲 body 发送给浏览器
                new_socket.send(html_content)
        else:
            # 2.2 如果请求的资源以 .py 结尾，那么就认为是动态资源的请求
            
            # body = ''
            # if file_name  == '/login.py':
            #     body = mini_frame.login()
            # elif file_name == "/register.py":
            #     body = mini_frame.register()
            
            env = dict()
            env['PATH_INFO'] = file_name
            # {'PATH_INFO': '/index.py'}
            
            # WSGI 框架
            body = self.application(env, self.set_response_header)  # 实现解耦

            header = f"HTTP/1.1 {self.status}\r\n"
            
            for temp in self.headers:
                header += f'{temp[0]}:{temp[1]}\r\n'
            
            header += '\r\n'
            response = header + body
            new_socket.send(response.encode('utf-8'))

        # 关闭套接字
        new_socket.close()
        
    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [("server", "mini_web v8.8")]
        self.headers += headers
    
    def run_forever(self):
        """用来完成整体的控制"""
        
        while True:
            #  4. 等待新客户端的连接
            new_socket, client_addr = self.tcp_server_socket.accept()
            
            # 5. 为这个客户端服务
            # 多进程子进程复制父进程的资源
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()
            
            new_socket.close()
        
        # 关闭监听套接字
        self.tcp_server_socket.close()


def main():
    """
    控制整体，创建一个 web 服务器对象，然后调用这个对象的 run_forever 方法运行
    :return:
    """
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])  # 7890
            frame_app = sys.argv[2]  # mini_frame:application
        except Exception as ret:
            print("端口输入错误...")
            return
    else:
        print("请按照以下方式运行")
        print("python3 xxx.py 7890 mini_frame:application")
        return

    ret = frame_app.split(":")
    frame_name = ret[0]
    app_name = ret[1]
    
    sys.path.append('./dynamic')
    # import frame_name  ----> 找 frame_name.py
    frame = __import__(frame_name)  # 返回值标记着 导入的这个函数
    app = getattr(frame, app_name)  # 此时 app 就指向了 dynamic/mini_frame 模块中的application函数
    
    wsgi_server = WSGIServer(port, app)
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()
