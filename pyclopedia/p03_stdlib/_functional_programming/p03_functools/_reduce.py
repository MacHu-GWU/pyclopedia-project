#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
syntax: ``reduce(function, iterable)``

reduce其实是将一系列数据, 按照function定义的方式合并汇总。其中function必须
有且只有两个输入参数, 并只返回一个值。例如::

    def add_two(a, b):
        return a + b
        
    res = reduce(add_two, [1, 2, 3, 4, 5]
    # 等价于
    res = ((((1 + 2) + 3) + 4) + 5)

注: 在Python2中, reduce曾经是内置关键字。但在Python3中被转移到functools模块下了。

Ref: 

- https://docs.python.org/3.3/library/functools.html#functools.reduce
"""

try:
    from functools import reduce
except ImportError:
    pass


def add_two(a, b):
    """add two number.
    """
    return a + b


def times_two(a, b):
    return a * b


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    assert reduce(add_two, array) == 15
    assert reduce(times_two, array) == 120
