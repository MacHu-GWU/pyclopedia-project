#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Update sql syntax.
"""

import sqlite3

connect = sqlite3.connect(":memory:")
cursor = connect.cursor()


def example():
    cursor.execute(
        "CREATE TABLE test (id INTEGER, name TEXTINTEGER, PRIMARY KEY (id));")
    records = [(1, "Alice"), (2, "Bob"), (3, "Cathy")]
    cursor.executemany("INSERT INTO test VALUES (?,?);", records)

    # Update Syntax
    cursor.execute("UPDATE test SET name = ? WHERE id = ?;", ("Jack", 2))
    cursor.execute("SELECT * FROM test WHERE id = 2;")
    assert cursor.fetchone() == (2, "Jack")

    # Update Syntax
    cursor.execute("UPDATE test SET name = ? WHERE id >= ?;", ("Tom", 1))

    for row in cursor.execute("SELECT * FROM test"):
        assert row[1] == "Tom"


if __name__ == "__main__":
    example()
    connect.close()
