#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``__missing__`` is been called by ``dict.__getitem__()`` to implement ``self[key]`` 
for dict subclasses when key is not in the dictionary.
  
**中文文档**

只有类是从dict继承而来的子类时, 在 ``__getitem__()`` 找不到key时, ``__missing__`` 才
会生效。综合看来, 这一特性用处不大。
"""


class SelfUpdateDict(dict):
    """A subclass of dict.
    """

    def __missing__(self, key):
        self[key] = None
        return self[key]


class MyList(object):
    """A custom list class.
    """

    def __init__(self):
        self.data = list()

    def append(self, value):
        self.data.append(value)

    def __getitem__(self, index):
        return self.data[index]

    def __missing__(self, index):
        """由于 ``MyList`` 不是从 ``dict`` 继承而来, 所以当 ``__getitem__`` 失效时, 
        并不会调用 ``__missing__`` 方法。
        """
        return None


if __name__ == "__main__":
    d = SelfUpdateDict({"a": 1, "b": 2})
    assert d["c"] is None

    mylist = MyList()
    mylist.append(1)
    try:
        mylist[10]  # __missing__ not been called
        raise Exception
    except IndexError as e:
        pass
