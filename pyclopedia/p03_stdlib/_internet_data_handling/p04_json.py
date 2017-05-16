#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python自带的标准json库实质上是一个json格式的解码器。能够灵活的在
str 和 dict 之间来回转换。所以访问dict中的值我们只能按照dict的方式
用dict[key]来访问

如果要用dict.key1.key2的方式来访问,则需要安装 jsontree 扩展包
https://pypi.python.org/pypi/jsontree/0.4.3, 但是目前不支持python3

relative reference:
    JSON versus XML, Chinese blog: http://www.cnblogs.com/SanMaoSpace/p/3139186.html
"""

import json


def example1():
    """Write json or dictionary into file
    step1: serialize dict to string
    step2: write string to file

    Notice:
        json.dumps(dict, ...) return a string
        json.dump(dict, file_object, ...) directly write string into a file
    """
    data = {1: ["a1", "a2"], 2: ["b1", "b2"]}
    print(json.dumps(data), type(json.dumps(data)))  # normal serialization
    print(json.dumps(data,                     # argv1 dict
                     sort_keys=True,           # argv2 sort_key
                     indent=4,                 # argv3 indent length
                     separators=(",", ": ")))  # argv4 separators
    """
    The following code equivalent to:
        with open("data.json", "w") as f:
            f.write(json.dumps(data) )
    """
    json.dump(data, open("data.json", "w"))

# example1()


def example2():
    """load json or dictionary from file
    step1: read the file
    step2: parse string to dict

    Notice:
        json.loads(string, ...) return a dict
        json.load(file_object, ...) directly return a dict from a file

    The following code equivalent to:
        with open("data.json", "r") as f:
            f.write(json.loads(data) )
    """
    print(json.load(open("data.json", "r")), type(
        json.load(open("data.json", "r"))))
    with open("data.json", "r") as f:
        print(json.loads(f.read()))

# example2()


def example3():
    """what kind of data is JSON serializable
    combination of: string, int, float, list, tuple, dictionary
                    True, False and None

    JSON doesn"t support set

    JSON Encoder will do:
        change all the string notation  to ",
        change all the tuple to list
    """
    data = {"name": "jack",  # success
            "age": 25,
            "children": ("Sam", "jack")}
    print(json.dumps(data, sort_keys=True, indent=4, separators=(",", ": ")))

    data = {"name": "jack",  # failure
            "age": 25,
            "children": ("Sam", "jack"),
            "pet": {"dog", "cat"}}
    print(json.dumps(data, sort_keys=True, indent=4, separators=(",", ": ")))

# example3()


def example4():
    # json还支持把字典和自定义的类建立联系。也就是用
    # {类名 : true, 属性名1: 属性值1, 属性名2: 属性值2, ...}
    # 来间接的表示一个类数据
    """ 把json字典按照类的定义格式输出 """
    def as_complex(dct):
        if "__complex__" in dct:
            return complex(dct["real"], dct["imag"])
        return dct

    print(json.loads(
        """{"__complex__": true, "real": 1, "imag": 2}""", object_hook=as_complex))

# example4()


from datetime import datetime
from bson.json_util import dumps

from sfm.nameddict import Base
import importlib

# class SuperJsonEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return {"__datetime__": obj.timestamp()}
#         else:
#         key = obj.__class__.__module__ + "." + obj.__class__.__name__
#         return {key: self.default(obj.__dict__)}
# return {key: super(SuperJsonEncoder, self).default(self, obj.__dict__)}
