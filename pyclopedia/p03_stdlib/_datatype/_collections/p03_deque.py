#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ref=https://docs.python.org/2/library/collections.html?highlight=ordereddict#collections.deque

""" 

双向链表 ``deque``:

1. 支持头尾插入，删除操作的链表。
2. 支持循环位移的环形链表。

而在初始化的时候，语句是： d = deque(iterable_object, max)
d是一个大小为max的双头FIFO，然后对iterable_object中的iter，填充到FIFO中

ref:

- https://docs.python.org/2/library/collections.html#collections.deque
- https://docs.python.org/3/library/collections.html#collections.deque
"""

import sys
from collections import deque


def example_create():
    """deque 的初始化
    """
    # 双向列表占用空间大，但插入删除速度快
    l = [1, 2, 3]
    d = deque([1, 2, 3])
    assert sys.getsizeof(l) < sys.getsizeof(d)

    # 像一个大小为3的 FIFO 一样，按照顺序填充deque
    d = deque([1, 2, 3, 4], 3)
    assert list(d) == [2, 3, 4]


example_create()


def example_method():  # [注意]请每次解除注销掉一个方法的代码进行演示
    """deque方法演示
    """
    # right append
    d = deque([1, 2, 3])
    d.append(4)
    assert list(d) == [1, 2, 3, 4]

    # left append
    d = deque([1, 2, 3])
    d.appendleft(4)
    assert list(d) == [4, 1, 2, 3]

    # right pop
    d = deque([1, 2, 3])
    d.pop()
    assert list(d) == [1, 2]

    # left pop
    d = deque([1, 2, 3])
    d.popleft()
    assert list(d) == [2, 3]

    # right append many
    d = deque([1, 2, 3])
    d.extend([4, 5])
    assert list(d) == [1, 2, 3, 4, 5]

    # left append many
    d = deque([1, 2, 3])
    d.extendleft([4, 5])
    assert list(d) == [5, 4, 1, 2, 3]

    # rotate
    d = deque([1, 2, 3])
    d.rotate(1)
    assert list(d) == [3, 1, 2]

    d.rotate(-1)
    assert list(d) == [1, 2, 3]


example_method()
