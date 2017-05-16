#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
try, except, else, finally

ref:

- https://docs.python.org/3/reference/compound_stmts.html#the-try-statement
- http://www.cnblogs.com/windlazio/archive/2013/01/24/2874417.html
"""

try:
    # Normal execution block
    pass
except ExceptionA:
    # Exception A handle
    pass
except ExceptionB:
    # Exception B handle
    pass
except:
    # Other exception handle
    pass
else:
    # if no exception, get here
    pass
finally:
    # this code will be executed anyway
    pass
