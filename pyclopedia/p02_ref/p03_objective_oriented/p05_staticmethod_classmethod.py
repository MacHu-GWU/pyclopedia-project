#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Calculator(object):
    # staticmethod没有self作为第一个变量, 本质上就是一个普通的函数。
    # staticmethod即可以从类本身调用, 也可以从实例调用。
    @staticmethod
    def add_two(a, b):
        return a + b


class User(object):

    def __init__(self, name=None, **kwargs):
        self.name = name

    # classmethod的第一个变量永远是类本身。
    # classmethod即可以从类本身调用, 也可以从实例调用。
    @classmethod
    def make_user(cls, data):
        return cls(**data)

    def make_user_bad_version(data):
        """This is a bad implement. Because it doesn't allows inherit.
        """
        return User(**data)


class SuperUser(User):
    pass


if __name__ == "__main__":
    assert Calculator.add_two(1, 2) == 3
    assert Calculator().add_two(1, 2) == 3

    assert User.make_user({"name": "Alice"}).name == "Alice"
    assert User(name="Alice").make_user({"name": "Bob"}).name == "Bob"

    # 对于继承而来的对象, 该功能失效了。
    assert isinstance(SuperUser.make_user_bad_version(
        {"name": "Cathy"}), SuperUser) is False
