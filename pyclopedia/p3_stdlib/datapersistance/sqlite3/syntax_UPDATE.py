##encoding=utf8

from __future__ import print_function
import sqlite3

def initial():
    connect = sqlite3.connect(":memory:")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE test (a INTEGER, b INTEGER, c REAL, d TEXT, PRIMARY KEY (a));""")
    return connect, cursor

def example1():
    conn, c = initial()
    records = [(i, i*10, i+0.01, "abc") for i in range(10)]
    c.executemany("INSERT INTO test VALUES (?,?,?,?);", records)
    
    c.execute("UPDATE test SET c = 9.9 * b WHERE a = 1;")
    for record in c.execute("SELECT * FROM test;"):
        print(record)
    
example1()