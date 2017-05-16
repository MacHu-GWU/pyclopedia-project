#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

keys = ["n%s" for i in range(1000000)]


def fromkeys():
    """dict.fromkeys is a very fast way to initial a dict that all keys 
    map to the same value. But the value should not be a mutable value if 
    you will edit the value.
    """
    st = time.clock()
    d = {key: 0 for key in keys}
    e1 = time.clock() - st

    st = time.clock()
    d = dict.fromkeys(keys, 0)
    e2 = time.clock() - st

    assert e1 > e2


fromkeys()


def get():
    """Try to get one item, if key not exist, then return default value.
    """
    d = dict(a=1, b=2)
    assert d.get("a") == 1
    assert d.get("b") == 2
    assert d.get("c") == None


get()


def setdefault():
    """Try to set one item, if key exist, then do nothing.
    """
    d = dict(a=1, b=2)
    d.setdefault("a", 3)
    d.setdefault("b", 3)
    d.setdefault("c", 3)
    assert d == {"a": 1, "b": 2, "c": 3}


setdefault()


def update():
    d = dict(a=1, b=1)
    d.update(dict(b=2, c=3))
    assert d == {"a": 1, "b": 2, "c": 3}


update()
