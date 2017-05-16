#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``__hash__(self)`` 定义了 hash(obj)的行为。
"""


class MyClass(object):
    def __init__(self, a):
        self.a = a

    def __hash__(self):
        return hash(self.a)

    def __eq__(self, other):
        return self.a == other.a


if __name__ == "__main__":
    m1 = MyClass("a")
    m2 = MyClass("a")

    s = set()
    s.add(m1)

    # set在添加一个元素时会判断是否定义了 __hash__ 方法, 以及有没有其他元素
    # 与之相等。所以s.add(m2)不会将m2添加进去。
    s.add(m2)
    assert len(s) == 1
