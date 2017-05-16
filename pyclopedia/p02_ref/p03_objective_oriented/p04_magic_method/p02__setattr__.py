#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
- ``__setattr__(self, attr, value)`` 实现了 x.attr = value 的行为。
"""


def example1():
    """False example, don't do this.

    **中文文档**

    这是因为在创建t = Tree()的时候, 调用了__init__中的self.data = dict()
    于是这个操作又调用了__setattr__(self, data, dict()), 而这时还没有创建
    self.data呢所以会提示找不到attribute data.

    总结: 一旦我们overwrite了__setattr__方法之后，在__init__中的所有属性的初始化
    赋值都会受到严重影响。解决的方法请看example2
    """
    class Tree(object):

        def __init__(self):
            # AttributeError: 'Tree' object has no attribute 'data'
            self.data = dict()

        def __setattr__(self, attr, value):
            self.data.setdefault(attr, value)

    try:
        t = Tree()
        raise Exception
    except AttributeError as e:
        pass


def example2():
    """A better example.

    **中文文档**

    由于Tree方法是从 ``object`` (Python的new style class的基类)继承而来。我们
    overwrite的是 ``Tree`` 中的 ``__setattr__`` 方法, 而 ``object.__setattr__`` 并不会
    被overwrite, 那么我们就可以用这个方法进行属性初始化。
    """
    class Tree(object):

        def __init__(self):
            object.__setattr__(self, "data", dict())

        def __setattr__(self, attr, value):
            self.data[attr] = value

    t = Tree()
    t.node1 = 1
    assert t.data == {"node1": 1}
    assert t.data["node1"] == 1

    # 问: 如果属性和本身内置属性冲突, 会发生什么?
    # 答: 并不会覆盖掉原本存在的属性, 而会正确的被赋值到字典中。这是因为在实例
    # 化之后的对象调用 x.attr = value 时, 会优先调用 x.__setattr__ 方法。
    t.data = 100
    assert t.data == {"node1": 1, "data": 100}


if __name__ == "__main__":
    example1()
    example2()
