#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Decorator is as simple as a syntax sugar for::

    @wrapper
        def myfunc(*args, **kwargs):
            ...
        
equals to::
    
    wrapper(myfunc)(*args, **kwargs)
"""

from __future__ import print_function
import time


def args_printer(func):
    """此包装器可以让任何函数在执行前打印该函数的输入参数信息, 执行后打印返回值。
    """
    def _wrapper(*args, **kwargs):
        text_args = ", ".join(["%r" % arg for arg in args])
        text_kwargs = ", ".join(["%s=%r" % (key, value)
                                 for key, value in kwargs.items()])
        print("+" + "-" * 100 + "+")
        print("Execute: %s(%s, %s)" % (func.__name__, text_args, text_kwargs))
        returns = func(*args, **kwargs)
        print("    Complete! Returns: %r." % returns)
        print("+" + "-" * 100 + "+")
        return returns

    return _wrapper


@args_printer
def print_message(message, indent=0):
    """此函数可以打印包含缩进的文本。
    """
    print("%s%s" % ("    " * indent, message))


print_message("Good Morning!", indent=4)


def execute_time_printer(func):
    """此包装器可以打印函数的输入参数信息, 执行后打印运行时间。
    """
    def _wrapper(*args, **kwargs):
        text_args = ", ".join(["%r" % arg for arg in args])
        text_kwargs = ", ".join(["%s=%r" % (key, value)
                                 for key, value in kwargs.items()])
        print("+" + "-" * 100 + "+")
        print("Execute: %s(%s, %s)" % (func.__name__, text_args, text_kwargs))
        st = time.clock()
        returns = func(*args, **kwargs)
        elapsed = time.clock() - st
        print("    Complete! Returns: %r; Elapsed %.6f seconds." %
              (returns, elapsed))
        print("+" + "-" * 100 + "+")
        return returns

    return _wrapper


@execute_time_printer
def mean(array):
    return sum(array) * 1.0 / len(array)


m = mean(list(range(10)))
assert m == 4.5
