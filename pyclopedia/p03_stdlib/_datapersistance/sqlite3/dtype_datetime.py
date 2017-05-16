#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python中的datetime.datetime类型在sqlite3中是TIMESTAMP, 而不是DATETIME。DATETIME
是字符串格式。
"""

import sqlite3
from datetime import datetime

# Create Connection
connect = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cursor = connect.cursor()

# Create Table
cursor.execute("CREATE TABLE log (id INTEGER, create_datetime DATETIME)")

# Insert Test Data
cursor.execute("INSERT INTO log VALUES (?, ?)", (1, datetime(2000, 1, 1),))

# Test
record = cursor.execute("SELECT * FROM log").fetchone()
assert record[1] == "2000-01-01 00:00:00"

connect.close()
