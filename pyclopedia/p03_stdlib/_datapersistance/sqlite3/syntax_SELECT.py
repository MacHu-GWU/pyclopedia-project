#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Select sql syntax.
"""

import sqlite3

connect = sqlite3.connect(":memory:")
cursor = connect.cursor()


def iter_cursor(cursor, arraysize=20):
    """fetch n data from cursor at each time. If query hits millions of data, 
    this will keep memory usage low.
    """
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            break
        for result in results:
            yield result


sql = \
    """
CREATE TABLE test
(id INTEGER PRIMARY KEY NOT NULL)
"""
cursor.execute(sql)
records = [(i,) for i in range(1000)]
cursor.executemany("INSERT INTO test VALUES (?)", records)


def example1():
    cursor.execute("SELECT * FROM test")
    assert len(list(cursor)) == 1000


example1()


def example2():
    cursor.execute("SELECT * FROM test")
    assert len(list(iter_cursor(cursor))) == 1000


example2()


if __name__ == "__main__":
    connect.close()
