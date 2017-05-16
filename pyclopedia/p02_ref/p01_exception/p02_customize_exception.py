#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exception is a class too.
"""

import random


class BaoZi(Exception):
    pass


class Big(Exception):
    pass


class Small(Exception):
    pass


def toss_dice():
    numbers = [1, 2, 3, 4, 5, 6]
    return [random.choice(numbers) for _ in range(3)]


def play():
    res = toss_dice()
    if res[0] == res[1] == res[2]:
        raise BaoZi("all %s: %s" % (res[0], res))

    try:
        if sum(res) >= 11:
            raise Big("big: %s" % res)
        else:
            raise Small("small: %s" % res)
    except Exception as e:
        #         print(e)
        pass


if __name__ == "__main__":
    play()
