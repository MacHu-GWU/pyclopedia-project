#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Insert sql syntax.
"""

import time
import random
import sqlite3

connect = sqlite3.connect(":memory:")
cursor = connect.cursor()


def example1():
    """Insert syntax example.
    """
    cursor.execute(
        "CREATE TABLE test1 (id INTEGER PRIMARY KEY NOT NULL, name TEXT, value REAL)")
    # 在sqlite3中 ? 相当于格式字符串输出符 %s
    cursor.execute(
        "INSERT INTO test1 VALUES (?, ?, ?)", (1, 'coke', 3.49))  # syntax1
    cursor.execute("INSERT INTO test1 VALUES (2, 'banana', 0.69)")  # syntax2
    cursor.execute(
        "INSERT INTO test1 (name, value) VALUES (?, ?)", ('apple', 5.19))  # syntax3
    cursor.execute(
        "INSERT INTO test1 (name, value) VALUES ('water', 1.35)")  # syntax4

    # 已插入4条记录
    cursor.execute("SELECT count(*) FROM test1")
    assert cursor.fetchone()[0] == 4


example1()


def example2():
    """Insert one by one vs bulk insert (``executemany`` method).
    """
    cursor.execute(
        "CREATE TABLE test21 (id INTEGER, value INTEGER, content TEXT);")
    cursor.execute(
        "CREATE TABLE test22 (id INTEGER, value INTEGER, content TEXT);")

    records = [
        (i, random.randint(1, 1000), "Hello World") for i in range(1000)
    ]

    st = time.clock()
    cursor.executemany("INSERT INTO test21 VALUES (?, ?, ?)", records)
    elapse1 = time.clock() - st

    st = time.clock()
    for record in records:
        cursor.execute("INSERT INTO test22 VALUES (?, ?, ?)", record)
    elapse2 = time.clock() - st

    assert elapse1 < elapse2


example2()


def example3():
    """Primary Key duplicate error handling in Python/sqlite3
    """
    cursor.execute(
        "CREATE TABLE test3 (id INTEGER PRIMARY KEY NOT NULL, number INTEGER)")

    records = [(1, 10), (3, 10), (5, 10)]  # insert some records at begin
    cursor.executemany("INSERT INTO test3 VALUES (?, ?)", records)

    records = [(2, 10), (3, 10), (4, 10)]
    try:
        cursor.executemany("INSERT INTO test3 VALUES (?, ?)", records)
    except:  # failed to batch insert, try normal iteratively insert
        for record in records:
            try:
                cursor.execute("INSERT INTO test3 VALUES (?, ?)", record)
            except:
                pass

    cursor.execute("SELECT count(*) FROM test3")
    assert cursor.fetchone()[0] == 5


example3()


if __name__ == "__main__":
    connect.close()
