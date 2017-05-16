#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ordered dictionaries are just like regular dictionaries but they 
remember the order that items were inserted.

ref:

- https://docs.python.org/2/library/collections.html?highlight=ordereddict#ordereddict-objects
- https://docs.python.org/3/library/collections.html?highlight=ordereddict#ordereddict-objects
"""

import sys
from collections import OrderedDict


def example():
    keys = "abcdefghijklmnopqrstuvwxyz"

    d = dict()
    for v, k in enumerate(keys):
        d[k] = v

    od = OrderedDict()
    for v, k in enumerate(keys):
        od[k] = v

    assert list(d) != list(keys)
    assert list(od) == list(keys)


if __name__ == "__main__":
    example()
