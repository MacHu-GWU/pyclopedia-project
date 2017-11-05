#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
klass.__bases__ return its base class in tuple.
"""


class A:
    pass


class B:
    pass


class C(A, B):
    pass


assert C.__bases__ == (A, B)

c = C()
try:  # instance doesn't have obj.__bases__
    c.__bases__
except AttributeError:
    pass
