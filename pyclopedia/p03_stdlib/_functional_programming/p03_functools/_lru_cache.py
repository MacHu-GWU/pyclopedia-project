#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LRU (least recently used) cache这种缓存能将函数最近N次被调用的输入参数和返回值
缓存起来, 每次有新的访问时, 会首先到缓存保存过的输入参数中查找, 如果找不到, 
才真正执行函数。

LRU缓存的典型应用场景是 **动态编程**, 或是 **IO为主要耗时的操作**。

例如著名的求 fibonacci 数列的动态编程解法就可以用到。 

又例如新闻客户端, 服务器缓存保存用户最近点击的1000篇新闻。由于最热的新闻一定
一直在缓存中保存着, 所以大量用户的请求将会落在这1000篇缓存文章中, 则可以大大
降低数据库的IO开销。

注: 此模块在Python3.2之后才出现.

Ref:

- https://docs.python.org/3.3/library/functools.html#functools.lru_cache
"""

import sys
import time


if sys.version_info >= (3, 2):
    import functools

    def fib1(n):
        """recursive solution for fibonacci(n).
        """
        if n < 2:
            return n
        return fib1(n - 1) + fib1(n - 2)

    def fib2(n):
        """dynamic programming solution for fibonacci(n).
        """
        if n <= 2:
            return 1
        i, res = 1, 1
        for _ in range(n - 2):
            i, res = res, res + i
        return res

    @functools.lru_cache(maxsize=32)
    def fib3(n):
        """use LRU cache and recursive solution for fibonacci(n).
        """
        if n < 2:
            return n
        return fib1(n - 1) + fib1(n - 2)

    n = 20

    #
    print("Call fib once...")
    st = time.clock()
    fib1(n)
    print("recursive: %.6f" % (time.clock() - st))

    st = time.clock()
    fib2(n)
    print("dynamic: %.6f" % (time.clock() - st))

    st = time.clock()
    fib3(n)
    print("cache: %.6f" % (time.clock() - st))

    #
    print("Call fib 1 to n...")
    st = time.clock()
    [fib1(i) for i in range(1, n + 1)]
    print("recursive: %.6f" % (time.clock() - st))

    st = time.clock()
    [fib2(i) for i in range(1, n + 1)]
    print("dynamic: %.6f" % (time.clock() - st))

    st = time.clock()
    [fib3(i) for i in range(1, n + 1)]
    print("cache: %.6f" % (time.clock() - st))

    #
    print("Call fib n many times...")
    st = time.clock()
    [fib1(n) for i in range(n)]
    print("recursive: %.6f" % (time.clock() - st))

    st = time.clock()
    [fib2(n) for i in range(n)]
    print("dynamic: %.6f" % (time.clock() - st))

    st = time.clock()
    [fib3(n) for i in range(n)]
    print("cache: %.6f" % (time.clock() - st))
