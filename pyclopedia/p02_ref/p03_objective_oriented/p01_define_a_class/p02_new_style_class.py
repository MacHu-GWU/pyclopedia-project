#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unless you need a constant container class like this::

    class Config:
        host = "127.0.0.1"
        port = 12345

Always make sure your class is inherited from ``object`` or subclass of 
``object``. Otherwise, compatibility issues may raises in Python2. 


ref: https://docs.python.org/2/reference/datamodel.html#new-style-and-classic-classes
"""


class User(object):

    def __init__(self, **kwargs):
        self._data = dict()
        for attr, value in kwargs.items():
            self._data[attr] = value

    def __setattr__(self, attr, value):
        if attr == "_data":
            if hasattr(self, "_data"):
                raise AttributeError(
                    "`%s` is not a valid attribute name." % attr)
            else:
                object.__setattr__(self, "_data", value)
        else:
            self._data[attr] = value

    def __getattribute__(self, attr):
        if attr == "_data":
            return object.__getattribute__(self, attr)
        else:
            return self._data[attr]


if __name__ == "__main__":
    import sys

    PY2 = sys.version_info.major == 2
    PY3 = sys.version_info.major == 3

    user = User(id=1, name="Alice")
    assert user.id == 1
    assert user.name == "Alice"
    assert user._data == {"id": 1, "name": "Alice"}

    try:
        user._data = {"id": 2, "name": "Bob"}
    except AttributeError:
        pass
