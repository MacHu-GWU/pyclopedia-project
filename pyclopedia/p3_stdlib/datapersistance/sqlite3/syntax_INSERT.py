##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-29             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

from __future__ import print_function
import sqlite3
import random
import time

def example1():
    '''sqlite3 基本INSERT语法'''
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("CREATE TABLE test (id INTEGER PRIMARY KEY NOT NULL, name TEXT, value REAL)")
    ## 在sqlite3中?相当于格式字符串输出符%s
    c.execute("INSERT INTO test VALUES (?, ?, ?)", (1, 'coke', 3.49) ) # syntax1
    c.execute("INSERT INTO test VALUES (2, 'banana', 0.69)") # syntax2
    c.execute("INSERT INTO test (name, value) VALUES (?, ?)", ('apple', 5.19) ) # syntax3
    c.execute("INSERT INTO test (name, value) VALUES ('water', 1.35)") # syntax4
    c.execute("SELECT * FROM test")
    for row in c.fetchall():
        print(row)
    
example1()

def example2():
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("CREATE TABLE test (id INTEGER, value INTEGER, content TEXT);")
    
    records = [(i, random.randint(10000, 20000), 'abcdefghijklmnopqrstuvwxyz' ) for i in xrange(1000000)]

    st = time.clock()
    c.executemany("INSERT INTO test VALUES (?, ?, ?)", records)
    print(time.clock() - st) # 1.49 ~ 1.57 for 1 million records
    
    st = time.clock()
    for record in records:
        c.execute("INSERT INTO test VALUES (?, ?, ?)", record)
    print(time.clock() - st) # 2.27 ~ 2.32 for 1 million records
    
# example2()

def example3():
    '''Graceful Primary Key Error handling in Python/sqlite3
    '''
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("CREATE TABLE test (id INTEGER PRIMARY KEY NOT NULL, number INTEGER)")
    records = [(1, 10), (3, 10), (5, 10)] # insert some records at begin
    c.executemany("INSERT INTO test VALUES (?, ?)", records)
    
    records = [(2, 10), (3, 10), (4, 10)]
    try:
        c.executemany("INSERT INTO test VALUES (?, ?)", records)
    except: # failed to batch insert, try normal iteratively insert
        for record in records:
            try:
                c.execute("INSERT INTO test VALUES (?, ?)", record )
            except:
                pass
            
    c.execute("SELECT * FROM test")
    for row in c.fetchall():
        print(row)

# example3()