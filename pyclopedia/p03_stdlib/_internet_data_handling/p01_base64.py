#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
base64是一种将任何二进制数据编码成ASCII字符的方法。其中Python提供了
urlsafe的版本, 使得编码结果中 ``-`` 会被 ``+`` 取代, ``_`` 会被 ``/`` 取代。
这样就不会出现url中禁止的字符了

Reference: https://docs.python.org/3/library/base64.html
"""

import base64


def test():
    """一个简单的用base64对数字编码的用例。
    """
    b = "Python".encode("ascii")

    assert base64.b16encode(b).decode("utf-8") == "507974686F6E"
    assert base64.b32encode(b).decode("utf-8") == "KB4XI2DPNY======"
    assert base64.b64encode(b).decode("utf-8") == "UHl0aG9u"

    assert base64.standard_b64encode(b).decode("utf-8") == "UHl0aG9u"
    assert base64.urlsafe_b64encode(b).decode("utf-8") == "UHl0aG9u"


if __name__ == "__main__":
    test()
