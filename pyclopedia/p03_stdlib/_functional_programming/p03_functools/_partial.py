#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
partial, 偏函数, 是函数式编程中的重要概念: 

当一个函数有参数a, b, c时。如果固定其中的某一个参数, 例如令 ``c = 10``。
我们通常需要使用 ``f(a, b, 10)`` 这样的形式。而通过偏函数, 我们可以创造出一个
新的函数 ``f_c_is_10(a, b)``, 然后直接调用之即可。这样做符合
Don't repeat yourself(DRY)原则。
"""

from functools import partial


def mod(int_a, int_b):
    """the mod of int_a % int_b.
    """
    if isinstance(int_a, int) and isinstance(int_b, int):
        return int_a % int_b


mod2 = partial(mod, int_b=2)
mod2.__doc__ = "mod 2"
mod10 = partial(mod, int_b=10)
mod10.__doc__ = "mod 10"


if __name__ == "__main__":
    assert mod2(17) == 1
    assert mod10(17) == 7
