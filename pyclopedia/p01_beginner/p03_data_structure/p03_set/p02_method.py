#!/usr/bin/env python
# -*- coding: utf-8 -*-

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Union
assert s1 | s2 == {1, 2, 3, 4, 5, 6}
assert set.union(s1, s2) == {1, 2, 3, 4, 5, 6}
assert s1.union(s2) == {1, 2, 3, 4, 5, 6}
assert set.union(s1, s1, s2, s2) == {1, 2, 3, 4, 5, 6}

# Intersection
assert s1 & s2 == {3, 4}
assert set.intersection(s1, s2) == {3, 4}
assert s1.intersection(s2) == {3, 4}
assert set.intersection(s1, s1, s2, s2) == {3, 4}

# Difference
assert s1 - s2 == {1, 2}
assert set.difference(s1, s2) == {1, 2}
assert s1.difference(s2) == {1, 2}

# Discard, remove one item
s = {1, 2, 3}
s.discard(2)
assert s == {1, 3}

# Pop, randomly pop one item and remove it
s = {1, 2, 3}
i = s.pop()
