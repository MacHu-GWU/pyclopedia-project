#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
当一个类继承自多个父类时, 如果多个父类(可能以及父类的父类)都定义了同一个方法,
那么调用这个类的这个方法时, 到底是在调用哪一个?

ref:

- 你真的理解Python中MRO算法吗？: http://python.jobbole.com/85685/
- https://docs.python.org/2/tutorial/classes.html#multiple-inheritance
- https://docs.python.org/3/tutorial/classes.html#multiple-inheritance
"""

from __future__ import print_function
import inspect
from pyclopedia.deco import run_if_is_main


@run_if_is_main(__name__)
def left_to_right():
    """width first, from left to right.
    """

    class A(object):
        name = "a"

        def method(self):
            return "a"

    class B(object):
        name = "b"

        def method(self):
            return "b"

    class C(A, B):
        pass

    assert C.name == "a"
    assert C().method() == "a"


left_to_right()


@run_if_is_main(__name__)
def width_first():
    """width first, from left to right.
    """

    class A(object):
        name = "a"

    class A1(object):
        pass

    class B(object):
        name = "b"

    class C(A1, B):
        pass

    assert C.name == "b"


width_first()


@run_if_is_main(__name__)
def c3_algorithm():
    """c3 algorithm demo.
    """

    class D(object):
        name = "d"

    class E(object):
        name = "e"

    class F(object):
        name = "f"

    class C(D, F):
        pass

    class B(E, D):
        pass

    class A(B, C):
        pass

    assert A.name == "e"
    assert B.name == "e"
    assert C.name == "d"

    print(A.__mro__)
    print(inspect.getmro(A))


c3_algorithm()
