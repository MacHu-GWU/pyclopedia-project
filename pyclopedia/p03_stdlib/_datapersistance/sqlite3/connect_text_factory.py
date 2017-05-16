#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在Python2中, 由于默认的字符串不是Unicode (UTF-8是Unicode中的一种最常用的编码),
所以在Python2中需要设置 ``connect.text_factory = str`` 才能够正确地读取non-ascii
字符串。
"""

import sqlite3

connect = sqlite3.connect(":memory:")
connect.text_factory = str  # Comment this makes this script fail in Python2
cursor = connect.cursor()

# Create Table
cursor.execute("CREATE TABLE log (id INTEGER, message TEXT)")

# Insert Test Data
cursor.execute("INSERT INTO log VALUES (?, ?)", (1, "中文"))

# Test
record = cursor.execute("SELECT * FROM log").fetchone()
assert record[1] == "中文"

connect.close()
