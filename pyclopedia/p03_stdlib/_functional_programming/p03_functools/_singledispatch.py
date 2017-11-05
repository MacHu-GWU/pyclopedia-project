#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
single dispatch是一种泛型函数的实现方式。泛型函数是一种为不同类型的参数执行
相似操作的函数组成的函数。相当于::

    def func(arg):
        if isinstance(arg, int):
            func_int(arg)
        elif isinstance(arg, float):
            func_float(arg)
        else:
            ...

ref:

- Python泛型函数与单分发器: http://www.10tiao.com/html/383/201610/2247483881/1.html
"""

import functools


@functools.singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


@fun.register(int)  # if first argument is int instance
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


@fun.register(float)  # if first argument is float instance
def fun_num(arg, verbose=False):
    if verbose:
        print("Half of your number:", end=" ")
    print(arg / 2)


@fun.register(list)  # if first argument is list instance
def _(arg, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)


def nothing(arg, verbose=False):  # if first argument is None
    print("Nothing.")


fun.register(type(None), nothing)

fun(1, verbose=True)
fun(3.14, verbose=True)
fun([1, 2, 3], verbose=True)
fun(None, verbose=True)
