#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
close是关闭connect的操作。在close的时候会自动rollback到上一次commit的状态。

由于sqlite是单线程写, 多线程读的设计。所以对于任意多connec读操作, 有没有
close都没有任何影响。而由于只有单线程写。所以其实有没有close所造成的影响只跟
上一次commit有关。所以其实不需要担心在多个连接同时存在时, 每个连接的任务完成后
是否关闭, 而只要在合适的时候commit即可。

Ref:

- http://stackoverflow.com/questions/9561832/what-if-i-dont-close-the-database-connection-in-python-sqlite
"""
