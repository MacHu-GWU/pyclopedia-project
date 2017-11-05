#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
API演示。
"""

from __future__ import print_function, unicode_literals
import time
import random
from heapq import *
from pyclopedia.deco import run_if_is_main


@run_if_is_main(__name__)
def performance_ordered_list():
    """测试堆在用于实现有序列表时的性能。

    有序列表是一种可以在末端进行append和pop操作, 并保持列表中的所有元素有序的
    数据结构。而有序列表的经典实现方式就是使用堆实现。每一次添加元素的操作的
    复杂度都为log(n)。下面的链接给出了Python的实现方式。

    Reference:

    - http://m.blog.csdn.net/article/details?id=51153423
    - http://www.yulongjun.com/2016/04/17/22-heap/
    """
    # initialize test data
    complexity = 1000
    array = list(range(complexity))
    random.shuffle(array)

    # heap implementation
    h = list()
    st = time.clock()
    for i in array:
        heappush(h, i)
    elapsed1 = time.clock() - st

    # sort the list every time after insert an item
    l = list()
    st = time.clock()
    for i in array:
        l.append(i)
        l.sort()
    elapsed2 = time.clock() - st

    # heap always faster than manual sort
    #     print("heap takes %.6f sec." % elapsed1)
    #     print("sort takes %.6f sec." % elapsed2)
    assert elapsed1 < elapsed2


performance_ordered_list()


@run_if_is_main(__name__)
def performance_sort():
    """测试堆排序和Python内置sort方法(快速排序)的性能。

    通常情况下堆排序的速度是和快速排序差不多的, 但是快速排序概率上的平均速度是
    所有排序算法中最优的。
    """
    # initialize test data
    complexity = 1000

    array = list(range(complexity))
    random.shuffle(array)

    # heap sort
    st = time.clock()
    h = list()
    for i in array:
        heappush(h, i)
    for i in range(len(array)):
        heappop(h)

    elapsed1 = time.clock() - st

    # built-in sort
    st = time.clock()
    array.sort()
    for i in array:
        pass

    elapsed2 = time.clock() - st

    # heap sort is slower
    #     print("heap sort takes %.6f sec." % elapsed1)
    #     print("list sort takes %.6f sec." % elapsed2)
    assert elapsed1 > elapsed2


performance_sort()


@run_if_is_main(__name__)
def performance_topK():
    """测试堆在求top K问题中的性能。
    """
    # initialize test data
    complexity = 1000
    array = list(range(complexity))
    random.shuffle(array)

    # heap top K
    st = time.clock()
    res = nlargest(3, array)  # 999, 998, 997

    elapsed1 = time.clock() - st

    # sort top K
    st = time.clock()
    array.sort()
    array[:3]

    elapsed2 = time.clock() - st

    # heap top K is faster
    #     print("heap topk takes %.6f sec." % elapsed1)
    #     print("sort takes %.6f sec." % elapsed2)
    assert elapsed1 < elapsed2


performance_topK()
