#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(Data Persistance) 数据持久层
===============================================================================
所谓数据持久是指在掉电, 关机之后仍然能保存数据的技术。换言之就是将复杂的数据结构
写入磁盘保存。这里面最为重要的几个库是:

- pickle: 将任何Python对象序列化
- sqlite3: sqlite数据库API
- bsddb: 一种高性能的Key, Value数据库
"""