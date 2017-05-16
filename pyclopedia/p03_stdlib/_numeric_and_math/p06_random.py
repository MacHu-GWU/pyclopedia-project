#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

ref:

- https://docs.python.org/2/library/random.html
- https://docs.python.org/3/library/random.html
"""

import random

options = "0123456789abcdefg"

# random choose one
choice = random.choice(options)

# choose non-repeat n, a combination from pool
md5 = "".join(random.sample(options * 32, 32))

# random integer 0 ~ 100
i = random.randint(0, 100)

# uniform distribution from [0.0, 1.0)
i = random.random()

# uniform distribution
i = random.uniform(0, 1)

# gauss distribution
i = random.gauss(0, 1)

# normal distribution
i = random.normalvariate(0, 1)
