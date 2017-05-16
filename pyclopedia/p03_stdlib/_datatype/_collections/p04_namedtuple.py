#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
namedtuple是一个高性能的数据容器类。占用的内存, 速度, 都比如下的代码要好很多::

    class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

ref: https://docs.python.org/2/library/collections.html?highlight=ordereddict#collections.namedtuple
"""

import sys
from collections import namedtuple


def example():
    Point = namedtuple("Point", "x, y", verbose=False)

    # Create
    p = Point(x=1, y=2)
    assert p.x == 1
    assert p.y == 2

    p = Point(**{"x": 1, "y": 2})
    assert p.x == 1
    assert p.y == 2

    p = Point._make([1, 2])
    assert p.x == 1
    assert p.y == 2

    # Method
    p = Point(x=1, y=2)
    assert p._fields == ("x", "y")
    assert p._asdict() == {"x": 1, "y": 2}

    # Return a new instance of the named tuple replacing specified fields
    # with new values
    assert p._replace(x=3).x == 3


example()


def extend():
    """This example shows how to extend namedtuple.
    """
    class BasePoint(object):
        @property
        def hypot(self):
            return sum([getattr(p, field) ** 2 for field in self._fields]) ** 0.5

    class Point(namedtuple("Point", "x, y, z", verbose=False), BasePoint):
        pass

    p = Point(x=1, y=1, z=1)
    assert abs(p.hypot - 1.732051) <= 0.001


extend()
