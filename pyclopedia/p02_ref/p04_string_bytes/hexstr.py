#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Hexstr是一种用16进制字符串来为二进制字节流编码的编码方式。比如在ASCII编码系统中::

    >>> ord("a")
    97 # 1100001

但在Hexstr系统中 "a" 代表 10, 也就是 1010。

Hexstr的一个常见应用场景就是MD5码。

MD5码是一个128位长的字节流。但为什么我们通常看到的MD5都是32位长的字符串呢? 这是
因为Hexstr能将4位的字节流转化成一个 ``"0123456789abcdef"`` 中的字符。
"""

import hashlib
import binascii


def example():

    with open(__file__, "rb") as f:
        content = f.read()

    m = hashlib.md5()
    m.update(content)

    b = m.digest()  # 128位字节流
    s = binascii.b2a_hex(b).decode("utf-8")  # 32位字符串
    assert s == m.hexdigest()  # .hexdigest() 方法能直接返回32位字符串


if __name__ == "__main__":
    example()
