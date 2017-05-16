#!/usr/bin/env python
# -*- coding: utf-8 -*-


def example1():
    """Slice operator.

    seq[::stride]         # [seq[0],   seq[stride],     ..., seq[-1]    ]
    seq[low::stride]      # [seq[low], seq[low+stride], ..., seq[-1]    ]
    seq[:high:stride]     # [seq[0],   seq[stride],     ..., seq[high-1]]
    seq[low:high:stride]  # [seq[low], seq[low+stride], ..., seq[high-1]]
    """
    l = list("01234567")
    assert l[::2] == list("0246")  # 从 index(0) 开始, 隔2个取一个
    assert l[1::2] == list("1357")  # 从 index(1) 开始, 隔2个取一个
    assert l[:4:2] == list("02")  # 从头开始到 index(4-1) 为止，隔2个取一个
    assert l[2:6:2] == list("24")  # 从index(2)开始到index(6-1)为止，隔2个取一个


example1()


def example2():
    """Reversed slice operator
    """
    l = list("01234567")
    assert l[::-1] == list("76543210")  # 从最后一个开始，逆序排列
    assert l[::-2] == list("7531")  # 从最后一个开始，隔2个取一个
    assert l[-2::-2] == list("6420")  # 从-2开始，隔2个取一个
    assert l[:3:-2] == list("75")  # 从最后开始，到3为止，隔2个取一个


example2()
