#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
klass.__mro__ return its base class in tuple.

.. note::

    Only new styled class (inheirt from ``object``) has ``.__mro__``
    magic attribute. In Python3 every class is new styled class by default.
"""


class D(object):
    pass


class E(object):
    pass


class F(object):
    pass


class C(D, F):
    pass


class B(E, D):
    pass


class A(B, C):
    pass


assert A.__mro__ == (A, B, E, C, D, F, object)

a = A()
try:  # instance doesn't have obj.__bases__
    a.__mro__
except AttributeError:
    pass
