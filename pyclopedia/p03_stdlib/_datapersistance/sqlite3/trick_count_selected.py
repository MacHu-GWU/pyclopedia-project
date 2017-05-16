#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
快速得到一个表中的行数, 或是选中的数据的行数。

结论: 使用 ``SELECT COUNT(*) FROM (SELECT column_name FROM test)``
"""

import time
import sqlite3

connect = sqlite3.connect(":memory:")
cursor = connect.cursor()

# Create Table
cursor.execute("CREATE TABLE test (id INTEGER)")

# Insert Test Data
n = 1000
records = [(i, ) for i in range(n)]
cursor.executemany("INSERT INTO test VALUES (?)", records)

# Bad Way
st = time.clock()
cursor.execute("SELECT * FROM test")
assert len(cursor.fetchall()) == n
elapse_slow = time.clock() - st

# Good Way
st = time.clock()
cursor.execute("SELECT count(*) FROM (SELECT id FROM test);")
assert cursor.fetchone()[0] == n
elapse_fast = time.clock() - st

assert elapse_fast < elapse_slow
