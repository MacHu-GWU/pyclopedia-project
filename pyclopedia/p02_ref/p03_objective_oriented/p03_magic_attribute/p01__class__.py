#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在Python中一切都是对象。任何对象在Python中都有__class__这个属性，其中储存的是
该对象所属的类。

在Python中有一个特殊的元类type，任何类的所属的类都是这个类继承过来的。
比如说list, dict, set这些对象都是从type继承而来的。

所以当一直进行 ``xxx.__class__.__class__.__class__...`` 之后, 最终都会指向 ``type``.
"""

import types

if __name__ == "__main__":
    number = 1
    assert number.__class__ is int
    assert type(number) is int
    assert number.__class__ is type(number)

    assert number.__class__.__class__ is type
    assert number.__class__.__class__.__class__ is type

    def add_two_number(a, b):
        return a + b

    assert add_two_number.__class__ is types.FunctionType
    assert add_two_number.__class__.__class__ is type
