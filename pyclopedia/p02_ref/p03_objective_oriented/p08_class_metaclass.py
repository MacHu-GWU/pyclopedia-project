#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
metaclass主要用于创建类定义本身(不是实例)。

ref:

- Stackoverflow 翻译1: http://blog.jobbole.com/21351/
- Stackoverflow 翻译2: http://pyzh.readthedocs.io/en/latest/python-questions-on-stackoverflow.html#metaclass
"""

from six import add_metaclass
from pyclopedia.deco import run_if_is_main


@run_if_is_main(__name__)
def example1():
    """
    当解释器执行完我们的类定义代码之后, 就会在类中寻找 klass.__metaclass__ 这一
    属性, 如果没有找到, 那么按照mro的方式在父类中寻找, 直到找到为止, 然后调用
    ``__metaclass__.__new__(cls, name, bases, attrs)`` 方法。
    """

    class Meta(type):
        def __new__(cls, name, bases, attrs):
            klass = super(Meta, cls).__new__(cls, name, bases, attrs)
            # Do some customize
            # ...
            return klass

    @add_metaclass(Meta)
    class Base(object):
        pass

    class MyClass(Base):
        pass


example1()


@run_if_is_main(__name__)
def example2():
    """本例中我们为所有从 ``Base`` 继承而来的类添加一个类属性 ``.classname``,
    即类名的字符串。
    """

    class Meta(type):
        def __new__(cls, name, bases, attrs):
            """
            :param cls: class it self
            :param name: class name
            :param bases: (BaseClass1, BaseClass2, ...)
            :param attrs: {attr1: value1, attr2: value2, ...} attr could be a
            method.
            """
            attrs["classname"] = name
            return super(Meta, cls).__new__(cls, name, bases, attrs)

    @add_metaclass(Meta)
    class Base(object):
        classname = None

    class User(Base):
        def __init__(self, name=None):
            self.name = name

    assert User.classname == "User"
    assert User().classname == "User"


example2()
