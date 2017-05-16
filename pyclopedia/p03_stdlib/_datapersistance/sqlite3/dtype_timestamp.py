#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python 提供为datetime.datetime对象提供了一个默认的adaptor。但是要启用这个adaptor
需要在创建connect的时候声明关键字 ``detect_types=sqlite3.PARSE_DECLTYPES``。
"""

import sqlite3
from datetime import datetime

# Create Connection
connect = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cursor = connect.cursor()

# Create Table
cursor.execute("CREATE TABLE log (id INTEGER, create_datetime TIMESTAMP)")

# Insert Test Data
cursor.execute("INSERT INTO log VALUES (?, ?)", (1, datetime(2000, 1, 1),))

# Test
record = cursor.execute("SELECT * FROM log").fetchone()
assert record[1] == datetime(2000, 1, 1)

connect.close()
