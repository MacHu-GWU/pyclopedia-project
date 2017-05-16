#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string


def construct_a_set():
    """Syntax: ``set(iterable)``
    """
    assert set([1, 2, 3]) == {1, 2, 3}
    assert set(range(3)) == {0, 1, 2}


construct_a_set()


def using_mutable_object_as_item_of_set():
    """By default, only integer, string and other hashable immutable built-in
    object can be item of a set. Any user defined object are not behave correctly.

    You could define ``__hash__`` method to make sure your object is hashable.
    Usually returns a integer or a string.
    """
    def random_text():
        return "".join([random.choice(string.ascii_letters) for i in range(32)])

    class Comment(object):

        def __init__(self, id, text):
            self.id = id
            self.text = text

        def __repr__(self):
            return "Comment(id=%r, text=%r)" % (self.id, self.text)

        def __hash__(self):
            return hash(self.id)

    l = [Comment(id=i, text=random_text()) for i in range(5)]
    s = set(l)
    for c in l:
        assert c in s


using_mutable_object_as_item_of_set()
