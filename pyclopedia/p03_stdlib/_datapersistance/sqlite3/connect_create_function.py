#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
create function可以自定义一个单输入单输出的函数供sql使用。
"""

import sqlite3


def add_one(i):
    return i + 1


connect = sqlite3.connect(":memory:")
connect.create_function("add_one", 1, add_one)
cursor = connect.cursor()
cursor.execute("select add_one(?)", (1,))
assert cursor.fetchone()[0] == 2

connect.close()
