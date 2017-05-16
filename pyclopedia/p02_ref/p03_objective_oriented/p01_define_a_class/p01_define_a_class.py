#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date


class Person(object):
    """``__init__`` method defines how you initiate an instance of the class.
    """

    def __init__(self, firstname, lastname, dob):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob

    def get_fullname(self):
        """define a method, ``self`` always be the first argument.
        """
        return "%s, %s" % (self.lastname, self.firstname)


if __name__ == "__main__":
    john_david = Person(
        firstname="David", lastname="John", dob=date(1985, 1, 1))
    assert john_david.get_fullname() == "John, David"
