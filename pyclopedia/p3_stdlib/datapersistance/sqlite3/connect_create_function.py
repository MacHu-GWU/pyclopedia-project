#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
create function可以自定义一个单输入单输出的函数供sql使用。
"""

import sqlite3

def add_one(i):
    return i + 1

con = sqlite3.connect(":memory:")
con.create_function("add_one", 1, add_one)
cur = con.cursor()
cur.execute("select add_one(?)", (1,))
assert cur.fetchone()[0] == 2