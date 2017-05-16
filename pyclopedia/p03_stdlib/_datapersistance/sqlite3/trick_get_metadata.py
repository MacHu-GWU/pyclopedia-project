#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

connect = sqlite3.connect(":memory:")
cursor = connect.cursor()

"""
在sqlite数据库中有一个隐藏的表格 ``sqlite_master``。一共有5列::

    CREATE TABLE sqlite_master (
        type TEXT, // 类别, 有 "table" 和 "index" 两种
        name TEXT, // 名称
        tbl_name TEXT, // 表名, 对于table而言, 就是名字本身。对于index而言, 是所属的table
        rootpage INTEGER, // 在内部表格中的序数, sqlite_master是第一个, 其他表格从2开始
        sql TEXT // 创建该表格的sql
    );

ref: https://www.sqlite.org/faq.html#q7
"""

cursor.execute("CREATE TABLE test1 (id INTEGER, date DATE)")
cursor.execute("CREATE TABLE test2 (id INTEGER, datetime DATETIME)")
cursor.execute("""SELECT name FROM sqlite_master WHERE type="table";""")
assert [record[0] for record in cursor.fetchall()] == ["test1", "test2"]

"""
在sqlite数据库中有一个内置的数据库级命令 ``PRAGMA``, 可以用子命令 
``table_info(table_name)`` 来查询表内各列的metadata::

    (
        column_id, // 列的序号, 从0开始
        column_name, // 列名
        data_type, // 数据类型
        not_null, // 0说明可以为Null, 1说明不可以为Null
        dflt_value, // 默认值
        is_primary_key, // 0不是主键, 1是主键
    )

ref: http://www.sqlite.org/pragma.html#pragma_table_info
"""
records = cursor.execute("PRAGMA table_info(test1)").fetchall()
assert records[0] == (0, 'id', 'INTEGER', 0, None, 0)
assert records[1] == (1, 'date', 'DATE', 0, None, 0)

records = cursor.execute("PRAGMA table_info(test2)").fetchall()
assert records[0] == (0, 'id', 'INTEGER', 0, None, 0)
assert records[1] == (1, 'datetime', 'DATETIME', 0, None, 0)
