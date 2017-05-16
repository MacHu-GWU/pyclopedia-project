#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
不同进制的整数。
"""

assert 0x1f == 31  # 16进制, 1 * 16 + 15
assert 0o21 == 17  # 8进制, 2 * 8 + 1
assert 0b11 == 3  # 2进制, 1 * 2 + 1

assert hex(31) == "0x1f"
assert oct(17) == "0o21"
assert bin(3) == "0b11"
