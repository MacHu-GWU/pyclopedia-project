#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在select操作中, cursor的fetchone, fetchall, fetchmany方法的区别。
"""

import sqlite3

connect = sqlite3.connect(":memory:")
cursor = connect.cursor()

# Create Table
cursor.execute("CREATE TABLE test (id INTEGER)")

# Insert Test Data
records = [(i, ) for i in range(1000)]
cursor.executemany("INSERT INTO test VALUES (?)", records)


def test_fetchone():
    """fetchone返回一个record, 如果没有record, 则返回None。
    """
    cursor.execute("SELECT * FROM test")
    assert cursor.fetchone()[0] == 0

    cursor.execute("SELECT * FROM test WHERE id > 9999")
    assert cursor.fetchone() is None


test_fetchone()


def test_fetchall():
    """fetchall将所有的record放到一个list中, 然后放在内存中一起返回。当数据量
    非常大时, 一次将所有数据读入内存不是一个好选择。

    直接对cursor进行for循环, 一次只会将一条数据放入内存返回, 而移动的只是文件
    系统上cursor的指针。
    """
    cursor.execute("SELECT * FROM test")
    i = -1
    for record in cursor.fetchall():  # Put everything into memory and return
        i += 1
        assert record[0] == i


test_fetchall()


def test_fetchmany():
    """fetchmany一次将指定数量的record放到一个list中返回。
    """
    cursor.execute("SELECT * FROM test")
    i = -1
    # Put n record into memroy one at a time
    for record in cursor.fetchmany(10):
        i += 1
        assert record[0] == i
    assert i == 10 - 1


test_fetchmany()
