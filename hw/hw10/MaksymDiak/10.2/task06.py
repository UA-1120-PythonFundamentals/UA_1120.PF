import re


def class_name_changer(cls, new_name):
    """Dynamic Classes"""
    if re.match(r"[A-Z][a-zA-Z0-9]+$", new_name):
        cls.__name__ = new_name
    else:
        raise Exception
