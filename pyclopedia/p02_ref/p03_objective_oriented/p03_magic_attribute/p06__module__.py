#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__module__的官方定义: `The name of the module the function was defined in, or 
None if unavailable. <https://docs.python.org/3.3/reference/datamodel.html#the-standard-type-hierarchy>`_。
中文解释: 类/函数 定义所在的模块。

只有 ``function``, ``class`` 对象有这个属性。被实例化的对象是没有这个属性的。
"""

import datetime


class Rectangle(object):
    """A rectangle class.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height


if __name__ == "__main__":
    assert Rectangle.__module__ == "__main__"
    assert datetime.datetime.__module__ == "datetime"

    dt = datetime.datetime(2014, 1, 1, 6, 30, 0)

    try:
        dt.__module__  # 实例没有__module__属性
        raise Exception
    except AttributeError as e:
        pass
