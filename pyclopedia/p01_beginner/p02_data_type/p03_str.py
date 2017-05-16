#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
String manipulate.
"""

# left strip
assert "  Hello  ".lstrip() == "Hello  "

# right strip
assert "  Hello  ".rstrip() == "  Hello"

# strip
assert "  Hello  ".strip() == "Hello"

# upper case
assert "Hello".upper() == "HELLO"

# lower case
assert "Hello".lower() == "hello"

# swap case
assert "Hello".swapcase() == "hELLO"

# titlize
assert "this is so good".title() == "This Is So Good"

# center
assert "Hello".center(9, "-") == "--Hello--"

# index
assert "this is so good".index("is") == 2

# replace
assert "this is so good".replace("is", "are") == "thare are so good"

# find
assert "this is so good".find("is") == 2

# count
assert "this is so good".count("o") == 3

# split
assert "This is so good".split(" ") == ["This", "is", "so", "good"]

# join
assert ", ".join(["a", "b", "c"]) == "a, b, c"

# ascii code to string
assert chr(88) == "X"

# string to ascii code
assert ord("X") == 88

# partition
assert "this is so good".partition("is") == ("th", "is", " is so good")

# make translate table and translate
table = str.maketrans("abc", "xyz")
assert "abc".translate(table) == "xyz"

# concatenate
assert "hello" + " " + "world" == "hello world"
