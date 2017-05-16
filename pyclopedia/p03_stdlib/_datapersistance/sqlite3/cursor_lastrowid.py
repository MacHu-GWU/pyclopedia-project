#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``cursor.lastrowid`` 返回最后一个使用 ``cursor.execute(sql)`` 进行的 Insert 
操作的行数。

ref: https://docs.python.org/2/library/sqlite3.html#sqlite3.Cursor.lastrowid
"""

import sqlite3

connect = sqlite3.connect(":memory:")
cursor = connect.cursor()

# Create Table
cursor.execute("CREATE TABLE test (id INTEGER, message TEXT)")

# Insert Test Data
records = [(i, None,) for i in range(1000)]
for record in records:
    cursor.execute("INSERT INTO test VALUES (?, ?)", record)

assert cursor.lastrowid == 1000

connect.close()
