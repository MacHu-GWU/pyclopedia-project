#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``functools.total_ordering`` 可以使得只需要定义 >, >=, <, <= 中的任意一个
以及 == 操作符, 那么就能自动定义全部的6种操作符。
"""

from functools import total_ordering


@total_ordering
class Student(object):
    """an example of using ``total_ordering``
    """

    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))

    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
