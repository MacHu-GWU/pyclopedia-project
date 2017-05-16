#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref:

- PY2: https://docs.python.org/2/library/functions.html#hex
- PY3: https://docs.python.org/3/library/functions.html#hex
"""

import copy


def immutable_object():
    """
    """
    i1 = 1
    i2 = 1
    assert id(i1) == id(i2)

    s1 = "abc"
    s2 = "abc"
    assert id(s1) == id(s2)


immutable_object()


def mutable_object():
    l1 = [1, 2]
    l2 = l1
    l3 = list(l1)

    assert id(l1) == id(l2)
    assert id(l1) != id(l3)


mutable_object()
