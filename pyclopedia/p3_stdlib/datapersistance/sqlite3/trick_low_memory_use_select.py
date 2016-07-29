#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
如何在当选择的数据量极大时, 避免将所有结果的数据放入内粗, 减少内存开销。

结论: 直接对cursor进行for循环即可。
"""

from pyclopedia.p3_stdlib.datapersistance.sqlite3 import connect, cursor

# Create Table
cursor.execute("CREATE TABLE test (id INTEGER)")

# Insert Test Data
records = [(i, ) for i in range(1000)]
cursor.executemany("INSERT INTO test VALUES (?)", records)

# Select
cursor.execute("SELECT * FROM test")
i = -1
for record in cursor: # for record in cursor is a generator
    i += 1
    assert record[0] == i