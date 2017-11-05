#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在Python中操作Mutable type(可变对象)时要小心, 一不留心就可能会出现Bug。

Reference: http://blog.csdn.net/lisonglisonglisong/article/details/38573269
"""

from __future__ import print_function, unicode_literals
import copy
from pyclopedia.deco import run_if_is_main


@run_if_is_main(__name__)
def common_in_shallow_and_deep_copy():
    """演示了shallow copy和deep copy的相同之处。
    """
    d = {"a": {"a1": 11, "a2": 12}, "b": {"b1": 21, "b2": 22}}
    d1 = copy.copy(d)
    del d1["a"]  # 在d1中删除key: "a"
    assert "a" in d  # "a"在d中并没有被删除

    d2 = copy.deepcopy(d)
    del d2["a"]  # 在d2中删除key: "a"
    assert "a" in d  # "a"在d中并没有被删除


common_in_shallow_and_deep_copy()


@run_if_is_main(__name__)
def difference_in_shallow_and_deep_copy():
    """演示了shallow copy和deep copy的不同之处。

    since shallow copy only copy object but not its members. In this case, the
    members are also dict, which is mutable. That's why d["a"]["a1"] is also
    deleted when you delete d1["a"]["a1"]

    由于shallow copy只拷贝对象, 但并不拷贝对象的成员。比如字典中的value就是成员。
    如果value本身是mutable的, 那么shallow copy就出问题了。而deepcopy会一直递归
    下去, 寻找所有的成员, 并在内存中重新创建一个副本。
    """
    d = {"a": {"a1": 11, "a2": 12}, "b": {"b1": 21, "b2": 22}}
    d1 = copy.copy(d)
    del d1["a"]["a1"]
    assert "a1" not in d["a"]  # "a1"在d中也被删除了

    d = {"a": {"a1": 11, "a2": 12}, "b": {"b1": 21, "b2": 22}}
    d1 = copy.deepcopy(d)
    del d1["a"]["a1"]
    assert "a1" in d["a"]  # "a1"在d中并没有被删除


difference_in_shallow_and_deep_copy()
