#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
for循环。

ref: https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
"""


def example():
    counter = 0
    for i in range(10):
        if i >= 7:
            continue
        counter += 1
    assert counter == 7

    counter = 0
    for i in range(10):
        if i >= 7:
            break
        counter += 1
    assert counter == 7


if __name__ == "__main__":
    example()
