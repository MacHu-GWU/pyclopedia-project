#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``cursor.rowcount`` 能返回上一次的写操作所影响的行数。
"""

from pyclopedia.p3_stdlib.datapersistance.sqlite3 import connect, cursor

# Create Table
cursor.execute("CREATE TABLE test (id INTEGER, message TEXT)")

# Insert Test Data
records = [(i, None,) for i in range(1000)]
cursor.executemany("INSERT INTO test VALUES (?, ?)", records)

# Row Count
assert cursor.rowcount == 1000 # Just Insert 1000 row

# Update
cursor.execute("UPDATE test SET message = ? WHERE id >= 500", ("Hello World!", ))
assert cursor.rowcount == 500 # Just Update 500 row

# # Select
for record in cursor.execute("SELECT * FROM test WHERE id >= 500"):
    assert record[1] == "Hello World!"