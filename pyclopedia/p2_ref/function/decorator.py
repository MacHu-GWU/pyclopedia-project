#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
装饰器是一种高阶函数在Python中的语法糖用法。高阶函数在之前的内容中已经介绍过。


@wrapper
def myfunc(*args, **kwargs):
    ...
    
相当于:

wrapper(myfunc)(*args, **kwargs)
"""

from __future__ import print_function
import time

def wrapper(func):
    """此包装器可以让任何函数在执行前打印该函数的输入参数信息, 执行后打印 "Complete!"。
    """
    def _wrapper(*args, **kwargs):
        text_args = ", ".join(["%r" % arg for arg in args])
        text_kwargs = ", ".join(["%s=%r" % (key, value) for key, value in kwargs.items()])
        print("+" + "-" * 100 + "+")
        print("Execute: %s(%s, %s)" % (func.__name__, text_args, text_kwargs))
        func(*args, **kwargs)
        print("    Complete!")
        print("+" + "-" * 100 + "+")
    return _wrapper

def timer_wrapper(func):
    def _wrapper(*args, **kwargs):
        st = time.clock()
        
        elapsed = time.clock() - st
        print()

@wrapper
def print_message(message, indent=0):
    """此函数可以打印包含缩进的文本。
    """
    print("%s%s" % ("    " * indent, message))

# print_message("Good Morning!", indent=1)


@timer_wrapper
def func():
    time.sleep(1)