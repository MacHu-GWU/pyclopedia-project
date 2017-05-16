#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
while条件循环。

ref: https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
"""


def example():
    i = 1
    total = 0
    while i <= 100:
        total += i
        i += 1
    assert total == 5050


if __name__ == "__main__":
    example()
