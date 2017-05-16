#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
本模块详细的剖析了Python中以**双下划线**开头的的成员名的特殊意义。

参考文章: 

- 博客: http://blog.csdn.net/gudesheng/article/details/2169038
- 官方文档: https://docs.python.org/3.3/tutorial/classes.html#private-variables
"""


def example1():
    """请观察以下代码, 并考虑assert部分的断言。
    """
    class A(object):

        def __init__(self):
            self.var_private = self.__private()
            self.var_public = self.public()

        def __private(self):
            return "A.__private()"

        def public(self):
            return "A.public()"

    class B(A):

        def __private(self):
            return "B.__private()"

        def public(self):
            return "B.public()"

    b = B()
    assert b.var_private == "A.__private()"
    assert b.var_public == "B.public()"
    assert b.public() == "B.public()"
    assert b._B__private() == "B.__private()"
    try:
        # an AttributeError will be raised
        assert b.__private() == "B.__private()"
        raise Exception
    except AttributeError:
        pass

    """
    类B从A继承了 ``__init__`` 方法, 但是覆盖了 ``__private`` 和 ``public`` 方法。
    但为什么最终只有 ``public`` 被成功覆盖了, 而 ``__private`` 却没有呢? 这是
    因为以双下划线开头的变量或者方法, 在Python中称作class-private members。其
    特性是, 在被继承的子类中原有的成员会成为父类的私有成员, 无法在子类中被覆盖。
    那么也许你会问了, 那么方法 ``B.__private`` 难道是被吞掉了吗? 这就要谈到
    Python中的私有变量轧压(Private name mangling)的机制。
    
    为了同时保留 ``A.__private`` 和 ``B.__private``, 编译器在生成代码前, 会对
    私有成员进行变量轧压, 已解决名称冲突的问题。具体的做法是在前面加上类名, 
    最后再加上一个下划线。例如 ``B.__private`` -> ``B._B__private``。
    
    这个机制达到了以下几个目的:

    1. Python中没有真正意义上的私有成员, 所以其实 ``A.__private`` 方法还是能通过
      ``A._A__private`` 从外部访问的。这样以另一种形式避免了直接从外部进行访问。
    2. 解决了命名空间冲突的问题。使得父类和子类中同名的私有成员可以共存。
    
    有两点需要注意的是:
    
    1. 因为轧压会使标识符变长，当超过255的时候，Python会切断，要注意因此引起的
      命名冲突。
    2. 当类名全部以下划线命名的时候，Python就不再执行轧压。如::
    
        from __future__ import print_function
    
        class ____(object):
            def __init__(self):
                self.__method()
                
            def __method(self):
                print("____.__method()")
    """


example1()


def example2():
    """一个变量轧压的应用。
    """
    # an application example
    class Mapping:

        def __init__(self, iterable):
            self.items_list = []
            self.__update(iterable)

        def update(self, iterable):
            for item in iterable:
                self.items_list.append(item)

        __update = update   # private copy of original update() method

    class MappingSubclass(Mapping):

        def update(self, keys, values):
            # provides new signature for update()
            # but does not break __init__()
            for item in zip(keys, values):
                self.items_list.append(item)

    # Mapping.update(self, iterable) been called
    m = MappingSubclass([1, 2, 3])  # now m.items_list = [1, 2, 3]

    # MappingSubclass(self, keys, values) been called
    # now m.items_list = [1, 2, 3, ('a', 1), ('b', 2), ('c', 3)]
    m.update("abc", [1, 2, 3])

    assert m.items_list == [1, 2, 3, ('a', 1), ('b', 2), ('c', 3)]

    """
    在 ``m = MappingSubclass([1, 2, 3])`` 初始化时, 调用的是 ``Mapping.__init__`` 中的
    ``Mapping.update`` 方法。而在 ``m.update("abc", [1, 2, 3])`` 中, 调用的是
    ``MappingSubclass.update`` 方法。这样就保证了 ``Mapping.__init__`` 中的
    ``Mapping.update`` 方法依然有效。
    """


example2()


def example3():
    """根据本例可以得知, 我们可以将在类的内部函数之间定义时所引用的, 但不允许
    用户在外部使用的变量用私有变量方式命名。比如pymongo中的 ``MongoClient``,
    ``Database``, ``Collection``. 每一个下级的概念都有一个变量绑定着上级概念。
    例如 ``Collection.__database = Database()``。而用户真正需要获得collection
    所绑定的database时可以使用下面的方法::

        @property
        def database(self):
            return self.__database
    """
    class A(object):

        """
        ``__private`` 是A的类私有变量, 只能在A的内部访问到。而一旦出了定义域, 
        就无法直接通过 ``.__private`` 直接访问到了。
        """
        __private = "private"
        public = "public"

        def __init__(self):
            self.private_var = self.__private
            self.public_var = self.public

    assert "public" in dir(A)
    assert "__private" not in dir(A)  # __private 已经不再存在了
    assert "_A__private" in dir(A)  # __private 被轧压成了 _A__private

    a = A()

    assert a.private_var == "private"
    assert a.public_var == "public"

    class B(object):

        """
        ``__private`` 是B的实例的私有成员。只能在类的定义中, 
        由 ``self.__private``直接访问到。一旦出了定义域, 就无法直接访问到了。
        """

        def __init__(self):
            self.__private = "private"
            self.public = "public"

        def get_private(self):
            return self.__private

    b = B()

    assert "public" in dir(b)
    assert "__private" not in dir(b)  # __private 已经不再存在了
    assert "_B__private" in dir(b)  # __private 被轧压成了 _B__private

    assert b.get_private() == "private"


example3()
