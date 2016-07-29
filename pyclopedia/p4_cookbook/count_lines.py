#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
How to count how many lines in a big pure text file?
    
**中文文档**

如何快速地计算有纯文本文件一共有多少行? 
"""

from __future__ import print_function, unicode_literals
import os
import time

fname = "bigfile.txt"


def create_test_file():
    with open(fname, "w") as f:
        f.write("\n".join([str(i)*80 for i in range(1000)]))


def remove_test_file():
    try:
        os.remove(fname)
    except Exception as e:
        print(e)


def get_file_lines1(fname):
    """generator method, yield, enumerate

    **中文文档**

    使用enumerate生成器, 对行号进行遍历, 最后一个行号+1即是行数。

    运行速度: 慢
    内存开销: 大
    """
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def get_file_lines2(fname):
    """built-in loop method in file object

    对文件中的行进行循环, 并统计行数。 该算法速度比较稳定。

    运行速度: 中等
    内存开销: 小
    """
    with open(fname) as f:
        i = 0
        for line in f:
            i += 1
            pass
        return i


def get_file_lines3(fname):  # BEST method with low memory consum
    """count "\n" using buffer method

    **中文文档**

    每次读取一小部分文本, 并统计换行符的个数。每次读取文本的数量会影响整体运行
    速度。

    运行速度: 快
    内存开销: 小
    """
    def block(file, size=65535):
        while 1:
            chunk = file.read(size)
            if not chunk:
                break
            yield chunk

    with open(fname, "r") as f:
        return sum(line.count("\n") for line in block(f)) + 1


def get_file_lines4(fname):
    """

    **中文文档**

    对文件进行遍历, 创建一个全1元素列表, 并求和。

    运行速度: 慢
    内存开销: 大
    """
    return sum(1 for line in open(fname))


def get_file_lines5(fname):
    """

    **中文文档**

    读取整个文件, 统计换行符个数。

    运行速度: 快
    内存开销: 大
    """
    with open(fname, "r") as f:
        return f.read().count("\n") + 1


def test_performance():
    create_test_file()

    method_list = [
        get_file_lines1,
        get_file_lines2, # Second best method, very stable.
        get_file_lines3, # Best method, but not stable.
        get_file_lines4,
        get_file_lines5,
    ]
    for i, method in enumerate(method_list):
        st = time.clock()
        count = method(fname)
        elapsed = time.clock() - st
        print("%s: %.6f sec, %s lines." % (i + 1, elapsed, count))

    remove_test_file()

test_performance()
