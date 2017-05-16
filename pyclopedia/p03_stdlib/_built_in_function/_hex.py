#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref:

- PY2: https://docs.python.org/2/library/functions.html#hex
- PY3: https://docs.python.org/3/library/functions.html#hex
"""

assert hex(255) == "0xff"
assert hex(-42) == "-0x2a"
assert float.hex(3.14) == "0x1.91eb851eb851fp+1"
assert float.hex(-0.618) == "-0x1.3c6a7ef9db22dp-1"
