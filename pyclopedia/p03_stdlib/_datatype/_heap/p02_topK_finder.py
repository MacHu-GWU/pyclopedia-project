#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
基于heap的, top_k问题解法。
"""

from __future__ import print_function, unicode_literals
import time
import random
import string
from heapq import *
from pyclopedia.deco import run_if_is_main


def create_test_data():
    n = 9999
    test_data = list()
    for _ in range(n):
        test_data.append(
            (
                random.randint(1, 1000000 + 1),
                "".join(random.sample(string.ascii_letters, 12)),
            )
        )
    return test_data


def heap_topK(iterable, n, key, reverse=False):
    """用堆排序获得topK问题的解。性能比sorted函数略好。
    """
    if reverse:
        return nlargest(n, iterable, key=key)
    else:
        return nsmallest(n, iterable, key=key)


@run_if_is_main(__name__)
def performance_heap_find_topK():
    """测试使用堆排序解决topK问题。

    sorted函数使用的就是堆排序, 所以两者性能基本等效, heap要略好。
    """
    # create test data
    test_data = create_test_data()
    k = 5

    # heap find topK
    st = time.clock()
    res1 = heap_topK(test_data, 5, key=lambda x: x[0], reverse=True)
    elapsed1 = time.clock() - st

    # built-in sorted find topK
    st = time.clock()
    res2 = sorted(test_data, key=lambda x: x[0], reverse=True)[:k]
    elapsed2 = time.clock() - st

    # heap always faster than manual sort
    #     print("heap topK elapse %.6f seconds" % elapsed1)
    #     print("sorted topK elapse %.6f seconds" % elapsed2)
    assert res1 == res2


performance_heap_find_topK()
