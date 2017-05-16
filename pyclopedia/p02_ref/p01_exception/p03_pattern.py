#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
There's several code patterns for exception handling.
"""


def divide1(a, b):
    """Manually exam to avoid error.
    """
    if b == 0:
        raise ValueError("Zero division Error!")
    return a * 1.0 / b


def divide2(a, b):
    """use ``try... except PossibleException... except`` clause.

    List all possible exception you can imagine, and leave other unpredictable
    exception to ``except clause``.
    """
    try:
        return a * 1.0 / b
    except ZeroDivisionError:
        raise ValueError("Zero division Error!")
    except Exception as e:
        raise e
