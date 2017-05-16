#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
How to get last raised exception, and it's detailed information
"""

import sys
import traceback


def get_last_exc_info():
    """This function can get last raised exception, 
    and return the formatted error message.
    """
    # exc_type, exception type
    # exc_value, the exception instance itself
    # exc_tb, exception trace back object
    exc_type, exc_value, exc_tb = sys.exc_info()

    # because trace back could be nested due to one exception are raised by
    # another exception. But the root one is always the first one.
    # ``traceback.extract_tb(exc_tb)`` can fetch the detail trace back info.
    for filename, line_num, func_name, code in traceback.extract_tb(exc_tb):
        tmp = ("{exc_value.__class__.__name__}: "
               "{exc_value}, appears in '{filename}' at line {line_num} in {func_name}(), code: {code}")
        info = tmp.format(
            exc_value=exc_value,
            filename=filename,
            line_num=line_num,
            func_name=func_name,
            code=code,
        )
        return info


def example():
    try:
        raise ValueError("1 is not a string!")
    except:
        info = get_last_exc_info()
        print(info)


if __name__ == "__main__":
    example()
