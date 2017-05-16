#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

**中文文档**

``defaultdict`` 能为还未出现在字典中的key自动赋一个默认值。常用于要对value进行
各种操作的场景。

ref:

- https://docs.python.org/2/library/collections.html#defaultdict-objects
- https://docs.python.org/3/library/collections.html#defaultdict-objects
"""

from collections import defaultdict


def example():
    """
    """
    d = defaultdict(lambda: 0)

    items = [("Alice", 1), ("Bob", 1), ("Alice", 1), ("Bob", 1)]
    for key, value in items:
        d[key] += 1

    assert d["Alice"] == 2
    assert d["Bob"] == 2


if __name__ == "__main__":
    example()
