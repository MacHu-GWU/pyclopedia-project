#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""
Math operator, 数学计算操作符。
"""

import sys
if sys.version_info.major == 2:
    PY2 = True
else:
    PY2 = False

# 加
assert 1 + 2 == 3

# 减
assert 2.5 - 1 == 1.5

# 乘
assert 2.5 * 4 == 10.0  # 小数 * 整数 变成小数

# 除
assert 12 / 3 == 4  # 整数 / 整数 如果能整除则还是整数

res = 10 / 4
if PY2:
    assert res == 2  # 整数 / 整数 如果不能整除, 在python2中是商向下取整
else:
    assert res == 2.5  # 整数 / 整数 如果不能整除, 在python3中是小数
assert 12.0 / 3 == 4.0  # 浮点数 / 整数 或 整数 / 浮点数 结果都是浮点数
assert 12 / 3.0 == 4.0  # 浮点数 / 整数 或 整数 / 浮点数 结果都是浮点数

# 余数
assert 10 % 3 == 1  # 余数
assert 10.5 % 3 == 1.5  # 余数可以是小数
assert -2 % 3 == 1  # 负数的余数是表示加几可以整除

# 乘方开方
assert 2 ** 3  # 乘方, 2的3次方
assert 2 ** 0.5  # 开方可以用乘方的形式来计算
