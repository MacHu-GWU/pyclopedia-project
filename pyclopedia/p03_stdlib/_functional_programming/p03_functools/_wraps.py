#!/usr/bin/env python
# encoding: utf-8

"""
在使用decorator时, 被装饰器装饰的函数, 其 __name__, __doc__, __module__会
继承wrapper函数的。这是因为::

    @decorator
    def func(*args, **kwargs):
        ...

等价于::

    decorator(func)(*args, **kwargs)

而如果我们使用了 ``functools.wraps`` 这个标准库, 就会使得装饰器不会改变函数
的这些私有属性。

ref:

- https://docs.python.org/2/library/functools.html#functools.update_wrapper
- https://docs.python.org/3/library/functools.html#functools.update_wrapper
"""

import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """This is docstring for wrapper.
        """
        return {"result": func(*args, **kwargs)}
    return wrapper


@my_decorator
def my_func():
    """This is docstring for my_func."""
    return

assert my_func() == {"result": None}

assert my_func.__name__ == "my_func"
assert my_func.__doc__ == "This is docstring for my_func."
