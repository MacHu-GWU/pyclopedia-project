#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create index sql syntax.
"""

import sqlite3
import time
import random

connect = sqlite3.connect(":memory:")
cursor = connect.cursor()


def example():
    # Create Table
    cursor.execute("CREATE TABLE test (id INTEGER, value INTEGER)")

    # Insert test data
    data = [(id, random.randint(1, 1000)) for id in range(1000)]
    cursor.executemany("INSERT INTO test VALUES (?,?)", data)
    connect.commit()

    # Query on Column("value") WITHOUT index
    st = time.clock()
    cursor.execute("SELECT * FROM test WHERE value >= 100 AND value <= 100")
    elapse1 = time.clock() - st

    # Create index on Column("value")
    cursor.execute("CREATE INDEX test_ind ON test (value)")
    connect.commit()

    # Query on Column("value") WITH index
    st = time.clock()
    cursor.execute("SELECT * FROM test WHERE value >= 400 AND value <= 600")
    elapse2 = time.clock() - st

    assert elapse1 > elapse2


if __name__ == "__main__":
    example()
    connect.close()
