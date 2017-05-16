#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Decorator is as simple as a syntax sugar for::

    @wrapper
        def myfunc(*args, **kwargs):
            ...
        
equals to::
    
    wrapper(myfunc)(*args, **kwargs)
    

**中文文档**

装饰器是一种高阶函数在Python中的语法糖用法。
"""

from __future__ import print_function


def example_function_can_nest():
    """In python, function is also an object. a function can return 
    another function.
    """
    def multiplier_k(k):
        def multiply(a):
            return a * k
        return multiply

    func = multiplier_k(10)
    assert func(1) == 10


example_function_can_nest()


def example_decorator():
    """Decorator is simply a syntax sugar to reduce the work of function 
    nesting. And have better readability.

    @wrapper
    def myfunc(*args, **kwargs):
        ...

    equals to:

    wrapper(myfunc)(*args, **kwargs)
    """
    def print_result(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print("Result is: %s" % result)
            return result

        return wrapper

    @print_result
    def add_two(a, b):
        return a + b

    assert add_two(1, 2) == 3


if __name__ == "__main__":
    example_decorator()
