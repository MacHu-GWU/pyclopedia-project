#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``cursor.description`` 是出于DB API 2.0的兼容性目的所创造的属性。 

ref: https://docs.python.org/2/library/sqlite3.html#sqlite3.Cursor.description
"""

from __future__ import print_function
import sqlite3

connect = sqlite3.connect(":memory:")
cursor = connect.cursor()

# Create Table
cursor.execute("CREATE TABLE test (id INTEGER)")

# Select
cursor.execute("SELECT * FROM test")
assert cursor.description == (('id', None, None, None, None, None, None),)
