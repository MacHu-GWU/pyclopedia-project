#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if sys.version_info >= (3, 2):
    def bytes_in_int():
        """bytes本质是二进制流, 那么一长串二进制数不也是一个非常大的整数吗?
        """
        i = int.from_bytes("a".encode("utf-8"), byteorder="big")
        i == 97

    bytes_in_int()

    def bytes_in_list():
        """字节流也可以每8个字节为一段, 分段地用一个列表来表示。
        """
        assert bytes([97, 98, 99]).decode("utf-8") == "abc"

    bytes_in_list()
