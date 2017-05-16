#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
sqlite是一款优秀的用于快速开发, 原型设计的数据库。麻雀虽小但五脏俱全。并且由于
使用了单线程写, 多线程读的机制, 并且没有用户组等复杂的东西, 所有代码用2万行C语言
写成, 使得它的速度要快于大多数的关系数据库。

Reference: 
- https://docs.python.org/2/library/sqlite3.html
- https://docs.python.org/3.4/library/sqlite3.html

Label:

- dtype: 数据类型
- trick: 小技巧
- syntax: 语法分析
- cursor: 游标相关
- connect: 连接相关
- database: 数据库相关
"""

import sqlite3

connect = sqlite3.connect(":memory:")
cursor = connect.cursor()
