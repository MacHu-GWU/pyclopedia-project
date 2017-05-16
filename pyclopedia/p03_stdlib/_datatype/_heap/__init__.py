#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
堆是一种特殊的二叉树, 其每个父节点的值都小于等于其子节点的值。如果从上往下, 从
左往右遍历整个堆, 返回的值是有序的。插入复杂度在 O(log(n)), 用于排序的复杂度在
O(nlog(n))。

堆的应用范围有:

1. 有序列表数据结构。
2. 堆排序。
3. 用来求Top-K问题。

Reference:
 
- https://docs.python.org/2/library/heapq.html
- https://docs.python.org/3/library/heapq.html
"""
