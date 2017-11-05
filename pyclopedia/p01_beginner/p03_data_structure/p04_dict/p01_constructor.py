#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dict Constructor
==============================================================================
"""

assert dict(a=1, b=2) == {"a": 1, "b": 2}
assert dict([("a", 1), ("b", 2)]) == {"a": 1, "b": 2}
assert dict({"a": 1, "b": 2}) == {"a": 1, "b": 2}