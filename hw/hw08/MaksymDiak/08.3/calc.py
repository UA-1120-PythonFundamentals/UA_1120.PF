import math
from math import pow


def area_of_rectangle(a, b):
    """Area of rectangle"""
    return a * b


def area_of_triangle(h, a):
    """Area of triangle"""
    return 0.5 * h * a


def area_of_circle(r):
    """Area of circle"""
    return math.pi * (pow(r, 2))
