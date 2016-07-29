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
import time
import random

def rand_string(length, mode = "alpha_digit"):
    """highest performance non-dependent pure python random string generator
    """
    # All the characters you want to use in your strings:
    if mode == "alpha_digit":
        test_chars = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    elif mode == "alpha":
        test_chars = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif mode == "alpha_digit_symbol":
        test_chars = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()`~-_=+"
    elif mode == "digit":
        test_chars = u"0123456789"
    return "".join(random.sample(test_chars, length))

conn = sqlite3.connect("test.db")
c = conn.cursor()

def example1():
    try:
        c.execute("CREATE TABLE test (ssn TEXT, value INTEGER, zipcode TEXT)")
        data = [(rand_string(32), random.randint(1, 1025), rand_string(5, mode="digit")) for i in range(1000000)]
        c.executemany("INSERT INTO test VALUES (?,?,?)", data)
        c.commit()
    except:
        pass
    
    st = time.clock()
    c.execute("SELECT * FROM test WHERE value >= 100 AND value <= 100")
    print(time.clock() - st)
    
    c.execute("CREATE INDEX test_ind ON test (value, zipcode)")
    
    st = time.clock()
    c.execute("SELECT * FROM test WHERE value >= 100 AND value <= 100")
    print(time.clock() - st)
 
example1()