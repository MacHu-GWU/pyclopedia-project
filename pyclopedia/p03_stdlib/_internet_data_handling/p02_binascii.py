#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
binascii这个库主要提供了binary数据和ascii数据之间的各种转化。

Reference:

- binascii: https://docs.python.org/3.3/library/binascii.html
- int.from_bytes: https://docs.python.org/3/library/stdtypes.html#int.from_bytes
"""

import binascii


def test_bytes_to_int():
    """本例提供了将任意的字符串, bytes和整数相互转换的方法。

    有的时候我们希望将bytes进行位操作, 进行一定的计算。比如在simhash中我们就要
    用到这个操作。这个时候就需要将任意对象转化为整数。
    """
    import six

    s = "a"
    b = s.encode("ascii")  # ord("a") = 97

    # 方法1, 将bytes转化为16进制数, 再转化为10进制数
    h = binascii.b2a_hex(b)  # b的二进制编码是97, 转化为16进制就是61 (6 * 16 + 1)
    assert int(h, 16) == 97

    # 方法2, 使用 int.from_bytes 方法, 只有Python3有此方法
    if six.PY3:
        assert int.from_bytes(b, "big") == 97


test_bytes_to_int()


def str_to_int(s):
    return int(binascii.b2a_hex(s.encode("utf-8")), 16)


def test_str_to_int():
    assert str_to_int("a") == 97


test_str_to_int()
