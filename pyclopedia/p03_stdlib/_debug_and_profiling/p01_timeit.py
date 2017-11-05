#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import timeit

try:
    range = xrange
except:
    pass
try:
    import numpy as np
except:
    pass


def wrapper(func, *args, **kwargs):
    def _wrapper():
        return func(*args, **kwargs)

    return _wrapper


def for_loop(n):
    for _ in range(n):
        pass


def eigenvalue(n):
    m = np.random.random((n, n))
    eigvalue, eigvector = np.linalg.eig(m)


if __name__ == "__main__":
    # elapsed = timeit.timeit(wrapper(for_loop, n=10**6), number=10)
    elapsed = timeit.timeit(wrapper(eigenvalue, n=256), number=10)
    print("elapsed %.6f" % elapsed)
