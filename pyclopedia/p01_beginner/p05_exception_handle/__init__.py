#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
try, except, else, finally

ref:

- https://docs.python.org/3/reference/compound_stmts.html#the-try-statement
- http://www.cnblogs.com/windlazio/archive/2013/01/24/2874417.html
"""

try:
    # Normal code block
    pass
except TypeError:
    # Exception 1 handle
    pass
except ValueError:
    # Exception 2 handle
    pass
except Exception as e:
    # Other exception handle, for example ``raise e``
    pass
else:
    # if no exception, get here
    pass
finally:
    # this code will be executed anyway
    pass
