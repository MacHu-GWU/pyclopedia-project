#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在sqlite3二进制对象的数据类型是BLOB。
"""

import sqlite3

connect = sqlite3.connect(":memory:")
cursor = connect.cursor()

# Create Table
cursor.execute("CREATE TABLE file (id INTEGER, binary BLOB)")

# Insert Test Data
cursor.execute("INSERT INTO file VALUES (?, ?)", (1, "Hello".encode("utf-8")))

# Test
record = cursor.execute("SELECT * FROM file").fetchone()
assert record[1] == b"Hello"

connect.close()
