#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

**中文文档**

所谓Immutable对象就是说, 对象一旦创建, 其中的属性, 值等内容是不可以以"任何"方式
被修改的。(这里的任何方式指的是一些常用的方式, 从根本上完全阻止修改是不可能的,
但是可以预防一些常见的修改形式) 所以这件事的关键就是对 ``__setattr__`` 这一方法
做出限制。

我们拿关系数据库中的数据行作为例子, 定义一个 ``ImmutableRow`` 对象。这个对象保存
了数据行中列名, 值的数据。其中值的数据可以通过: ``ImmutableRow.column`` 或是
``ImmutableRow["column"]`` 两种形式访问。但是其所有的属性都不允许被修改。

也就是说::

    row = ImmutableRow(columns=("a", "b"), values=(1, 2))
    row.a = 100 # not allowed
    row.b = 100 # not allowed
    row.c = 100 # not allowed

"""

from collections import OrderedDict


class ImmutableRow(object):
    def __init__(self, keys, values):
        d = OrderedDict()
        for key, value in zip(keys, values):
            object.__setattr__(self, key, value)
            d[key] = value
        object.__setattr__(self, "data", d)

    def __setattr__(self, attr, value):
        raise AttributeError("ImmutableRow does not allow attribute editing.")

    def __setitem__(self, key, value):
        raise AttributeError("ImmutableRow does not allow attribute editing.")

    def __getitem__(self, key):
        return self.__getattribute__(key)

    @property
    def keys(self):
        return self.data.keys()

    @property
    def values(self):
        return self.data.values()

    @property
    def items(self):
        return self.data.items()


if __name__ == "__main__":
    row = ImmutableRow(("a", "b"), (1, 2))

    assert row.a == 1
    assert row["b"] == 2
    assert row.data == {"a": 1, "b": 2}
    assert list(row.items) == [("a", 1), ("b", 2)]

    try:
        row.a = 100
        raise Exception
    except AttributeError as e:
        pass

    try:
        row["b"] = 100
        raise Exception
    except AttributeError as e:
        pass
