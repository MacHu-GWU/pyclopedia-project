#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tinynumpy是一个纯Python的numpy库实现, 功能虽然不够强大, 但是胜在部署相当方便。

https://github.com/wadetb/tinynumpy
"""

from __future__ import print_function
from tinynumpy import tinynumpy as tnp

m = tnp.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m1 = tnp.ones(m.shape)
m2 = tnp.zeros(m.shape)

def sub_matrix():
    print(m[0, :])
    print(m[:, 0])
    print(m[0:2, 0:2])

# sub_matrix()

def math_operation():
    print(m + m)
    print(m + m1)
    print(m1 + m2)
    print(m - m)
    print(m - m1)
    print(m1 - m2)
    print(m * m)
    print(m * m1)
    print(m1 * m2)
    print(m / m)
    print(m / m1)
    
    print(m // m)
    print(m // m1)
    print(m % m)
    print(m % m1)

    print(tnp.dot([1, 2], [4, 5]))
    print(tnp.dot([1, 2, 3], [4, 5, 6]))

math_operation()

def handle_none():
    """TinyNumpy can NOT handle None.
    """
    a = tnp.array([1, None, 3])
    
# handle_none()
