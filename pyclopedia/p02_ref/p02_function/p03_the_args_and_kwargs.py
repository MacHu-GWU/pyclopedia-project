#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``func(*args, **kwargs)`` can takes undefined parameters (kwargs is for keyword
style parameters). 

ref: https://docs.python.org/2/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another

**中文文档**

Python中的函数传递参数的形式有以下四种, 可以搭配组合起来使用:

1. 普通参数。
2. 带默认值的参数。
3. 任意多个的列表性参数。
4. 任意多个的关键字的字典型参数。
"""

import six


def test_args_and_kwargs():
    if six.PY2:
        pass

    if six.PY3:
        # Notice: this is not allowed in Python2
        def func(a, *args, b=1, **kwargs):
            return a, args, b, kwargs

        a, args, b, kwargs = func(1, 2, 3, b=4, c=5)
        assert a == 1
        assert args == (2, 3)
        assert b == 4
        assert kwargs == {"c": 5}

        a, args, b, kwargs = func(1, *(2, 3), b=4, **{"c": 5})
        assert a == 1
        assert args == (2, 3)
        assert b == 4
        assert kwargs == {"c": 5}


if __name__ == "__main__":
    test_args_and_kwargs()
