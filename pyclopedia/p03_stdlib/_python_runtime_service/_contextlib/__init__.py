#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

ref:

- https://docs.python.org/2/library/contextlib.html
- https://docs.python.org/3/library/contextlib.html
- http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001478651770626de401ff1c0d94f379774cabd842222ff000

"""

import contextlib


def contextmanager():
    """Context的写法是::

        @contextlib.contextmanager
        def func(*args, **kwargs)
            # do something
            yield var # with func(*args, **kwargs) as var
            # do something
    """
    class Connect(object):

        def __enter__(self):
            print("Begin")
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            if exc_type:
                print("Error")
            else:
                print("Complete")

        def execute(self, e=None):
            if e is not None:
                raise e

    class Connect(object):

        def execute(self, e=None):
            if e is not None:
                raise e

    @contextlib.contextmanager
    def create_connect(*args, **kwargs):
        print('Begin')
        conn = Connect()
        yield conn  # as conn
        print("Complete")

    with create_connect() as conn:
        conn.execute()

# contextmanager()


def execute_some_code_before_and_after():
    """contextmanager可以使得执行任意代码的前后, 都执行一些指定代码。
    """
    @contextlib.contextmanager
    def before_and_after():
        print("Before")
        yield
        print("After")

    with before_and_after():
        print("Doing")

# execute_some_code_before_and_after()


def closing():
    """

    **中文文档**

    如果一个对象没有事项 ``__enter__``, ``__exit__`` 方法, 但是实现了 
    ``close()`` 方法, 我们就可以用 ``contextlib.closing(obj) as var`` 的语法, 
    使得在离开代码块时, 自动调用 ``obj.close()`` 方法。 
    """
    try:
        from urllib import urlopen
    except:
        from urllib.request import urlopen

    with contextlib.closing(urlopen('http://www.python.org')) as page:
        for line in page:
            pass
        # page.close() method will automatically been called at the end


closing()
