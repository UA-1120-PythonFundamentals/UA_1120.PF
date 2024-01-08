""" doc for func"""
# import math
# year = 1986


# def print_year():
#     print(year)

# def sin(x):
#     return f"sin({x})={math.sin(x)}"


from math import sin as _sin

year = 1986


def print_year():
    print(year)


def sin(x):
    return f"sin({x})={_sin(x)}"

if __name__ == "__main__":
    print(__name__ ,dir())