#!/usr/bin/env python


import pytest


class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    obj1 = Man()
    obj2 = Woman()

    return [obj1, obj2]


def test_god_man():
    paradise = God()
    assert isinstance(paradise[0], Man) == True, "First object is a man"


def test_god_woman():
    paradise = God()
    assert isinstance(paradise[1], Woman) == True, "Second object is a woman"

def test_first_obj_parent_class():
    paradise = God()
    assert "Human" in str(paradise[0].__class__.__base__), "First object has Human as parent class"

def test_second_obj_parent_class():
    paradise = God()
    assert "Human" in str(paradise[1].__class__.__base__), "Second object has Human as parent class"
