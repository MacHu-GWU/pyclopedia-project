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
import os

fname = 'employee.db'
conn = sqlite3.connect(fname) # 连接到本地数据库文件
c = conn.cursor()

c.execute(\
"""CREATE TABLE employee
(
ID INTEGER PRIMARY KEY NOT NULL,
name TEXT NOT NULL,
email TEXT NOT NULL,
position TEXT NOT NULL,
ann_salary INTEGER NOT NULL
)
""")

conn.commit() # 确认保存
conn.close() # 关闭连接
os.remove(fname)