#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
本模块是一个用heapq实现priority queue(优先队列)数据结构的例子。优先队列是指,
在当有序队列中的元素有相同的值时, 返回那个先进入队列的元素。这个数据结构实现起来
有很多小陷阱, 下面给出的是Python官方的实现。

Ref:

- 什么是优先队列: https://en.wikipedia.org/wiki/Priority_queue
- 用Heap的实现: https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes
"""

from __future__ import print_function
from heapq import *
import itertools
from pyclopedia.deco import run_if_is_main

pq = []  # list of entries arranged in a heap
entry_finder = {}  # mapping of tasks to entries
REMOVED = "<removed-task>"  # placeholder for a removed task
counter = itertools.count()  # unique sequence count


def add_task(task, priority=0):
    "Add a new task or update the priority of an existing task"
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)


def remove_task(task):
    "Mark an existing task as REMOVED.  Raise KeyError if not found."
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    "Remove and return the lowest priority task. Raise KeyError if empty."
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task, priority
    raise KeyError("pop from an empty priority queue")


@run_if_is_main(__name__)
def test():
    import string
    import random
    import time

    def randstr():
        res = list()
        for _ in range(8):
            res.append(random.choice(string.ascii_letters))
        return "".join(res)

    tasks = [(randstr(), random.randint(1, 3)) for _ in range(5)]
    """
    [("xxx", 1 ~ 5), ...]
    """
    st = time.clock()

    print("--- Task in ---")
    for task in tasks:
        add_task(*task)
        print(task)

    print("--- Task out ---")
    for _ in range(len(pq)):
        print(pop_task())

    print("heap takes %.6f sec." % (time.clock() - st,))


test()
