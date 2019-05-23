#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 19:59
# @Author  : Paulson
# @File    : 1-闭包.py
# @Software: PyCharm
# @define  : function

# 问题：初中里学过函数，例如 y=kx+b, y=ax^2 + bx + c
# 以y=kx+b为例，请计算一条线上的过个点 即 给x值 计算出y值

# 第1种
# k = 1
# b = 2
# y = k*x+b
# 缺点：如果需要多次计算，那么就的写多次y = k*x+b这样的式子

# 第2种
def line_2(k, b, x):
	print(k*x+b)

line_2(1, 2, 0)
line_2(1, 2, 1)
line_2(1, 2, 2)
# 缺点：如果想要计算多次这条线上的y值，那么每次都需要传递k，b的值，麻烦

print("-"*50)


# 第3种: 全局变量
k = 1
b = 2
def line_3(x):
	print(k*x+b)

line_3(0)
line_3(1)
line_3(2)
k = 11
b = 22
line_3(0)
line_3(1)
line_3(2)
# 缺点：如果要计算多条线上的y值，那么需要每次对全局变量进行修改，代码会增多，麻烦

print("-"*50)

# 第4种：缺省参数
def line_4(x, k=1, b=2):
	print(k*x+b)

line_4(0)
line_4(1)
line_4(2)

line_4(0, k=11, b=22)
line_4(1, k=11, b=22)
line_4(2, k=11, b=22)
# 优点：比全局变量的方式好在：k, b是函数line_4的一部分 而不是全局变量，因为全局变量可以任意的被其他函数所修改
# 缺点：如果要计算多条线上的y值，那么需要在调用的时候进行传递参数，麻烦

print("-"*50)

# 第5种：实例对象
class Line5(object):
	def __init__(self, k, b):
		self.k = k
		self.b = b

	def __call__(self, x):
		print(self.k * x + self.b)


line_5_1 = Line5(1, 2)
# 对象.方法()
# 对象()
line_5_1(0)
line_5_1(1)
line_5_1(2)
line_5_2 = Line5(11, 22)
line_5_2(0)
line_5_2(1)
line_5_2(2)
# 缺点：为了计算多条线上的y值，所以需要保存多个k, b的值，因此用了很多个实例对象， 浪费资源

print("-"*50)

# 第6种：闭包

def line_6(k, b):
	def create_y(x):
		print(k*x+b)
	return create_y


line_6_1 = line_6(1, 2)
line_6_1(0)
line_6_1(1)
line_6_1(2)
line_6_2 = line_6(11, 22)
line_6_2(0)
line_6_2(1)
line_6_2(2)



# 思考：函数、匿名函数、闭包、对象 当做实参时 有什么区别？
# 1. 匿名函数能够完成基本的简单功能，，，传递是这个函数的引用 只有功能
# 2. 普通函数能够完成较为复杂的功能，，，传递是这个函数的引用 只有功能
# 3. 闭包能够将较为复杂的功能，，，传递是这个闭包中的函数以及数据，因此传递是功能+数据
# 4. 对象能够完成最为复杂的功能，，，传递是很多数据+很多功能，因此传递是功能+数据


































