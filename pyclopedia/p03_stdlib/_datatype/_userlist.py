#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

from six import PY3
if PY3:
    from collections import UserDict, defaultdict
else:
    from collections import defaultdict
    from UserDict import UserDict


class Tree(defaultdict):
    def __init__(self, *args, **kwargs):
        super(Tree, self).__init__(Tree, *args, **kwargs)

    def __setattr__(self, attr, value):
        self[attr] = value

    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            return self[name]


usa = Tree(name="USA")
usa.population = 100
print(usa.population)
# md = Tree(name="MD")
