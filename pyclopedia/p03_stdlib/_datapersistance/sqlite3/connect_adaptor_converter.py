#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
由于sqlite默认只支持int, float, str, date, datetime, bytes, null几种数据类型, 
对于其他数据类型, 可以通过函数将其他数据类型与几种内置数据类型相互转化。只要
注册了转换器函数即可。转换器函数通常使用bytes作为接口, 但使用其他类型比如int
也是可以的。

- adapter: 把其他类型转化为内置类型
- converter: 把内置类型转化为其他类型

在Python sqlite3中有两个默认的adaptor: datetime.date, datetime.datetime。可以
将这两个类型与字符串自动转化。
"""

import sqlite3


class Point(object):

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "Point(%.2f, %.2f)" % (self.x, self.y)

    def __gt__(self, other):
        if self.x > other.x and self.y > other.y:
            return True
        else:
            return False


def adapter_point(point):
    return ("(%.2f, %.2f)" % (point.x, point.y)).encode("ascii")


def converter_point(text):
    x, y = list(map(float, text[1:-1].split(b", ")))
    return Point(x, y)


def test_adapter_converter():
    point = Point(4.0, 6.0)
    text = adapter_point(point)
    assert text == b"(4.00, 6.00)"

    point1 = converter_point(text)
    assert abs(point1.x - 4.0) <= 0.0001
    assert abs(point1.y - 6.0) <= 0.0001


test_adapter_converter()


# Register adapter and converter
sqlite3.register_adapter(Point, adapter_point)
sqlite3.register_converter("point", converter_point)


# Create Connection, Insert Test Data
connect = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cursor = connect.cursor()
connect.execute("CREATE TABLE test (p point)")
connect.execute("INSERT INTO test VALUES (?)", (Point(4.0, 6.0),))


# Select Point
point = connect.execute("SELECT * FROM test").fetchone()[0]
assert abs(point.x - 4.0) <= 0.0001
assert abs(point.y - 6.0) <= 0.0001


# Another Select Point
# 虽然在Point中定义了比较符, 但是Sql中的 p > Point(3.0, 7.0)实际上是用
# "(3.00, 7.00)" 去与 "(4.00, 6.00)" 的字符串形式比较。所以满足了条件, 返回了
# Point(4.00, 6.00)。但是实际上根据 __gt__()中的定义, 是并不满足的。
# 所以使用adapter的情况下, WHERE或者一切sql函数的操作对象都是adapter的返回值。
point = connect.execute(
    "SELECT * FROM test WHERE p > ?", (Point(3.0, 7.0), )).fetchone()[0]
assert abs(point.x - 4.0) <= 0.0001
assert abs(point.y - 6.0) <= 0.0001
