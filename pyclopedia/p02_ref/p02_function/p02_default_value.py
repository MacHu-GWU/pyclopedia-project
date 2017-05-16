#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
function parameter with default value (in case the param is not given).
"""


def add(a, increament=1):
    return a + increament


if __name__ == "__main__":
    assert add(0) == 1
