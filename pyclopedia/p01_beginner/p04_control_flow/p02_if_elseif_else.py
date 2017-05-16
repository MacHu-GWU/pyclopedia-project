#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
if, elif, else条件判定。

ref: https://docs.python.org/3/tutorial/controlflow.html#if-statements
"""


def example():
    def validate(value):
        if value > 0:
            return "pos"
        elif value < 0:
            return "neg"
        else:
            return "zero"

    assert validate(1) == "pos"
    assert validate(-1) == "neg"
    assert validate(0) == "zero"


if __name__ == "__main__":
    example()
