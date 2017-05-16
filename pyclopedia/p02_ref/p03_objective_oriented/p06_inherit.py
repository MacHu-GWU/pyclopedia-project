#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

继承是面向对象中非常重要的概念。

继承是指当子类从父类继承而来时, 自动获得父类中定义的所有属性和方法。当然子类
可以重新定义父类中的属性和方法, 这叫做覆盖(override)。

ref:

- https://docs.python.org/2/tutorial/classes.html#inheritance
- https://docs.python.org/3/tutorial/classes.html#inheritance
"""


class A(object):
    a1 = "a1"

    @property
    def a2(self):
        return "a2"

    def method(self):
        return "method_a"

    @staticmethod
    def static_method():
        return "staticmethod_a"

    @classmethod
    def class_method(cls):
        return cls.__name__


class B(A):

    def method(self):
        return "method_b"


if __name__ == "__main__":
    assert B.a1 == "a1"
    assert B().a2 == "a2"
    assert B().method() == "method_b"
    assert B.class_method() == "B"
