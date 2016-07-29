#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sqlite3

def iterC(cursor, arraysize = 10):
    'An iterator that uses fetchmany to keep memory usage down'
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            break
        for result in results:
            yield result
            
conn = sqlite3.connect(":memory:")
c = conn.cursor()
cmd = \
"""
CREATE TABLE test
(id INTEGER PRIMARY KEY NOT NULL)
"""
c.execute(cmd)
records = [(i,) for i in xrange(1000)]
c.executemany("INSERT INTO test VALUES (?)", records)

def example1():
    c.execute("SELECT * FROM test")
    for row in c.fetchall():
        print(row)

example1()

def example2():
    c.execute("SELECT * FROM test")
    for row in iterC(c): # 生成器模式，对于结果很多的查询可以避免把所有结果读到内存中
        print(row)
        
example2()
    




