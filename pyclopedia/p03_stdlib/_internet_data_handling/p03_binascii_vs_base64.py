#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python标准库中为 ``base64 encoding`` 提供了两个库: 
`binascii <https://docs.python.org/3/library/binascii.html>`_ 和
`base64 <https://docs.python.org/3/library/base64.html>`_.
都可以用来做base64编码, 推荐使用base64

本文档测试了:

1. 这两个库得到的结果是不是完全一样? (是)
2. 这两个库的速度到底哪个更快? (差不多)
"""


import time

import string
import random

import binascii
import base64


def random_string(length=32, charset=string.hexdigits):
    return "".join([random.choice(charset) for _ in range(length)])


def test_behave():
    """Test how 'bytes to string and string to bytes' behave.

    Conclusion: binascii.b2a_base64 and base64.b64encode are doing same things.
    """
    s = random_string()
    b = s.encode("utf-8")

    # binascii
    # string, b2a_base64 has a 'newline' at the end
    s_binascii = binascii.b2a_base64(b).decode("utf-8")
    b_binascii = binascii.a2b_base64(s.encode("utf-8"))  # bytes

    # base64
    s_base64 = base64.b64encode(b).decode("utf-8")  # string
    b_base64 = base64.b64decode(s.encode("utf-8"))  # bytes

    assert s_binascii.strip() == s_base64.strip()
    assert b_binascii == b_base64


test_behave()


def test_performance():
    """Module binascii vs base64.

    Conclusion: binascii is faster than base64.
    """

    data = [random_string().encode("utf-8") for i in range(10000)]

    st = time.clock()
    for b in data:
        binascii.b2a_base64(b)
    elapse_binascii = time.clock() - st

    st = time.clock()
    for b in data:
        binascii.b2a_base64(b)
    elapse_base64 = time.clock() - st

    # 两者速度相差不到10%
    assert abs(elapse_binascii - elapse_base64) / elapse_base64 <= 0.1


test_performance()
