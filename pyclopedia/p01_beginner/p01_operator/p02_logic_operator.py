#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Logic operator, 逻辑运算操作符。
"""

# 与
assert (True & True) == True
assert (True & False) == False
assert (False & True) == False
assert (False & False) == False

assert (True and True) == True
assert (True and False) == False
assert (False and True) == False
assert (False and False) == False

# 或
assert (True | True) == True
assert (True | False) == True
assert (False | True) == True
assert (False | False) == False

assert (True or True) == True
assert (True or False) == True
assert (False or True) == True
assert (False or False) == False

# 非
assert (not True) == False
assert (not False) == True

assert (not True) == False
assert (not False) == True
