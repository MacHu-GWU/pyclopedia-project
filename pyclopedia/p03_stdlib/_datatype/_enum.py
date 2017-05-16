#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref:

- 官方文档: https://docs.python.org/3/library/enum.html
- 非官方教程: http://www.pandacademy.com/enum-%E6%9E%9A%E4%B8%BE%E7%B1%BB%E5%9E%8B/
"""

import sys

if sys.version_info >= (3, 4):
    from enum import Enum

    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
