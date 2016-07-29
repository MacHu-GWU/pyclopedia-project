#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
rollback机制是数据库中最重要的机制之一。有了它数据库的完整性才能得到保证。
rollback的功能是恢复到最近一次commit()的状态
"""

from pyclopedia.p3_stdlib.datapersistance.sqlite3 import connect, cursor


def test_rollback():
    cursor.execute("CREATE TABLE test (id INTEGER, name TEXT)")
    connect.commit()  # 此时表中无数据

    # 插入一条数据
    cursor.execute("INSERT INTO test VALUES (?,?)", (1, "bob"))
    assert len(cursor.execute("SELECT * FROM test").fetchall()) == 1

    # 回到了表中无数据的状态
    connect.rollback()
    assert len(cursor.execute("SELECT * FROM test").fetchall()) == 0

    connect.close()

test_rollback()
