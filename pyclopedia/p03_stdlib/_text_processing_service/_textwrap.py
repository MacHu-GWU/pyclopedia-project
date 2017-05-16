#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
textwrap提供了以下功能:

1. 字符串按照指定宽度自动换行
2. 字符串等间距增加或取消缩进
3. 将字符串截断为定长

ref:

- https://docs.python.org/2/library/textwrap.html
- https://docs.python.org/3/library/textwrap.html
"""

from __future__ import print_function
import textwrap


def wrap_and_fill():
    """wrap能将文本按照每行不超过n个字符串的规则分行。
    """
    text = ("The textwrap module provides two convenience functions, wrap() and "
            "fill(), as well as TextWrapper, the class that does all the work, "
            "and two utility functions, dedent() and indent(). If you’re just "
            "wrapping or filling one or two text strings, the convenience "
            "functions should be good enough; otherwise, you should use an "
            "instance of TextWrapper for efficiency.")

    print("-" * 80)
    print(text)

    print("-" * 80)
    print("\n".join(textwrap.wrap(text, width=80)))

    print("-" * 80)
    print(textwrap.fill(text, width=80))

wrap_and_fill()


def indent_and_dedent():
    text = \
        """
for i in range(10):
    print(i)
    """
    print("-" * 80)
    print(text)

    print("-" * 80)
    indented_text = textwrap.indent(text, "    ")
    print(indented_text)

    print("-" * 80)
    dedented_text = textwrap.dedent(indented_text)
    print(dedented_text)

indent_and_dedent()


def shorten():
    """shorten能将多余的空格压缩至一个, 并能将文本截断至定长。
    """
    print(textwrap.shorten("Hello  world!", width=12))
    print(textwrap.shorten("Hello  world!", width=11))
    print(textwrap.shorten("Hello  world!", width=10, placeholder="..."))

shorten()
