#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import inspect


# print(inspect.getargspec(func))

if sys.version_info > (3, 4):
    def signature():
        """

        **中文文档**

        ``inspect.signature(callable)`` 能获得一个callable函数的输入参数和输出
        值的信息。可以知道有哪些输入参数, 以及他们的默认值(如果有的话)

        ref: https://docs.python.org/3/library/inspect.html#inspect.signature
        """
        def func(a, b, c=1, **kwargs):
            return a + b

        sig = inspect.signature(func)
        assert sig.parameters["a"].default is inspect._empty
        assert sig.parameters["b"].default is inspect._empty
        assert sig.parameters["c"].default == 1
        assert sig.parameters["kwargs"].default is inspect._empty

    signature()
