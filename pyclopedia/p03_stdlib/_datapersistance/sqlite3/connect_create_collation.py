#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
collation还研究的不是特别清楚。
"""

import sqlite3


def collate_reverse(string1, string2):
    if string1 == string2:
        return 0
    elif string1 < string2:
        return 1
    else:
        return -1


connect = sqlite3.connect(":memory:")
connect.create_collation("reverse", collate_reverse)

cursor = connect.cursor()
cursor.execute("create table test(x)")
cursor.executemany("insert into test(x) values (?)", [("a",), ("b",)])
cursor.execute("select x from test order by x collate reverse")

for row in cursor:
    #     print(row)
    pass

connect.close()
