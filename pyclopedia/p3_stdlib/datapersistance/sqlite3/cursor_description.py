#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``cursor.description`` 是出于DB API 2.0的兼容性目的所创造的属性。 
"""

from pyclopedia.p3_stdlib.datapersistance.sqlite3 import connect, cursor

# Create Table
cursor.execute("CREATE TABLE test (id INTEGER)")

# Select
cursor.execute("SELECT * FROM test")
print(cursor.description)