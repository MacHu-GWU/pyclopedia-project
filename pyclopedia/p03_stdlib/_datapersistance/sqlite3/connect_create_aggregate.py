#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
create aggregate可以自定义一个对单列的值进行批量计算的函数。

ref: https://www.sqlite.org/lang_expr.html#collateop
"""

import sqlite3


class TotalScore:

    def __init__(self):
        self.total_score = 0

    def step(self, score):
        self.total_score += score

    def finalize(self):
        return self.total_score


con = sqlite3.connect(":memory:")
con.create_aggregate("totalscore", 1, TotalScore)
cur = con.cursor()
cur.execute("CREATE TABLE evaluate (name TEXT, score INTEGER)")
cur.execute("INSERT INTO evaluate VALUES (?, ?)", ("Bob", 70))
cur.execute("INSERT INTO evaluate VALUES (?, ?)", ("Jack", 80))
cur.execute("INSERT INTO evaluate VALUES (?, ?)", ("Mike", 90))
cur.execute("select totalscore(score) from evaluate")
assert cur.fetchone()[0] == 240
