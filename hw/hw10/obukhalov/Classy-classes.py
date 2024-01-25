#!/usr/bin/env python

import pytest


class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"


@pytest.mark.parametrize(
    ("name", "age"), [("john", 16), ("matt", 25), ("alex", 57), ("cam", 39)]
)
def test_person_class_constructor(name, age):
    person = Person(name, age)
    test_info = name + "s" + " age is " + str(age)
    assert person.info == test_info
