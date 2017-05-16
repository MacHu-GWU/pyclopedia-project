#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``__call__`` 定义了 obj()的行为。

也就是::

    >>> myclass = MyClass()
    >>> myclass(*args, *kwargs) # call myclass.__call__(*args, *kwargs) method
    ...
"""


class FallingDistanceCalculator(object):
    """distance = 0.5 * g * t * t calculator
    """

    def __init__(self, g):
        self.g = g

    def __call__(self, t):
        return (self.g * t ** 2) / 2


if __name__ == "__main__":
    g = 9.8
    calculator = FallingDistanceCalculator(g)
    seconds = 3.0
    dist = calculator(seconds)
    assert abs(dist - g * seconds ** 2 / 2) <= 0.001
