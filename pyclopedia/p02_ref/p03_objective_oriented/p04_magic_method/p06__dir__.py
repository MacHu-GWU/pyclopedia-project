#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``__dir__`` 方法定义的是 dir(class)的行为, 返回的是class的所有方法名和属性名
"""

from datetime import datetime

if __name__ == "__main__":
    assert "year" in dir(datetime)
    assert "strftime" in dir(datetime)
    assert "strptime" in dir(datetime)
