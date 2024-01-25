#!/usr/bin/env python


import pytest


class ClassNameError(Exception):
    pass


def class_name_changer(cls, new_name):
    if new_name.isalnum() and new_name[0].isupper():
        cls.__name__ = new_name
    else:
        raise ClassNameError(
            "Class name must contains upper & lower letters plus ciphers, and starting only with upper case letter."
        )


def test_original_class_name():
    class MyClass:
        pass

    myObject = MyClass()
    assert MyClass.__name__ == "MyClass", "Original name is MyClass"


def test_first_class_name_change():
    class MyClass:
        pass

    myObject = MyClass()
    class_name_changer(MyClass, "UsefulClass")
    assert MyClass.__name__ == "UsefulClass", "Original name is UsefulClass"


def test_second_class_name_change():
    class MyClass:
        pass

    myObject = MyClass()
    class_name_changer(MyClass, "SecondUsefulClass")
    assert MyClass.__name__ == "SecondUsefulClass", "Original name is SecondUsefulClass"


def test_wrong_class_name_1():
    class MyClass:
        pass

    myObject = MyClass()

    with pytest.raises(ClassNameError):
        class_name_changer(MyClass, "abc123")


def test_wrong_class_name_2():
    class MyClass:
        pass

    myObject = MyClass()

    with pytest.raises(ClassNameError):
        class_name_changer(MyClass, "Abc123#")
