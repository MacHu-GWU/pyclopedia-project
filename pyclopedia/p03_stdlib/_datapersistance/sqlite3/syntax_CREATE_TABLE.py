#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create table sql syntax.
"""

import sqlite3

connect = sqlite3.connect(":memory:")
cursor = connect.cursor()


def example():
    sql = \
        """
    CREATE TABLE employee
    (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    salary INTEGER NOT NULL
    )
    """

    cursor.execute(sql)

    assert len(list(cursor.execute("PRAGMA table_info(employee)"))) == 4


if __name__ == "__main__":
    example()
    connect.close()
