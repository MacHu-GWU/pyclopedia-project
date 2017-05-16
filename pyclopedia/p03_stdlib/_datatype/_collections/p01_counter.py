#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Counter 可以理解为一个频率统计计数器。实际上是一个字典的子类, 具有
``{key: counts}`` 这样的数据结构。

1. 支持从可迭代对象中生成counter。
2. 和dict一样有 ``keys()``, ``values()``, ``items()``这些方法。
3. 很方便的往容器里批量添加、删除元素。
4. 支持数学操作符运算。

ref:

- https://docs.python.org/2/library/collections.html#counter-objects
- https://docs.python.org/3/library/collections.html#counter-objects
"""

from __future__ import print_function
from collections import Counter


def construct():
    """Initialize a Counter.
    """
    # a new, empty counter
    c = Counter()

    # a new counter from an iterable, items has to be comparable
    c = Counter("abbccc")
    assert c["a"] == 1

    # a new counter from a mapping
    c = Counter({"red": 4, "blue": 2})
    assert c["red"] == 4

    # a new counter from keyword args
    c = Counter(cats=4, dogs=8)
    assert c["cats"] == 4


construct()


def getitem():
    """
    """
    c = Counter("abbccc")

    # get a item exists
    assert c["a"] == 1

    # get a item not exists, returns 0
    assert c["d"] == 0

    # Counter is dict like object, support keys(), values(), items().
    c.keys()
    c.values()
    c.items()

    elements = list(c.elements())
    elements.sort()
    assert elements == list("abbccc")


getitem()


def method():
    c = Counter("abbccc")
    assert c.most_common(3) == [("c", 3), ("b", 2), ("a", 1)]

    # 从 abbccc 中减去了 ab，相当于减法,和 c - Counter("ab")不同的是，保留负值
    c.subtract("ab")
    assert c["a"] == 0
    assert c["b"] == 1

    # 从 bccc 中加上了 ab，相当于加法
    c.update("ab")
    assert c["a"] == 1
    assert c["b"] == 2


method()


def math_operation():
    """ some math operation in between two counter
    """
    c1 = Counter(a=3, b=1)
    c2 = Counter(a=1, b=2)

    # add two counters together
    c3 = c1 + c2
    assert c3["a"] == 4
    assert c3["b"] == 3

    # subtract (keeping only positive counts)
    c3 = c1 - c2
    assert c3["a"] == 2
    assert c3["b"] == 0

    # intersection:  min(c1[x], c2[x])
    c3 = c1 & c2
    assert c3["a"] == 1
    assert c3["b"] == 1

    # union:  max(c1[x], c2[x])
    c3 = c1 | c2
    assert c3["a"] == 3
    assert c3["b"] == 2


math_operation()
