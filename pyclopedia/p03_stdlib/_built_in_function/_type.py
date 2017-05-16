#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref: 

- PY2: https://docs.python.org/2/library/functions.html#type
- PY3: https://docs.python.org/3/library/functions.html#type
"""


def as_get_class_type_function():
    """``type(a_instance)`` can get the type of a instance.
    """
    assert type(1) is int
    assert type("Good") is str


as_get_class_type_function()


def as_class_factory_function():
    """``type`` can create a class define statement dynamically.

    Syntax: ``type(classname, inherit_from_class_tuple, attribute_dict)``
    """

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "%s(name=%r)" % (self.__class__.__name__, self.name)

    User = type("User", (), {"__init__": __init__, "__repr__": __repr__})

    user = User(name="Jack")
    assert user.name == "Jack"
    assert str(user) == "User(name='Jack')"


as_class_factory_function()
