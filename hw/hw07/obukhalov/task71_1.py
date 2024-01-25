#!/usr/bin/env python


def largest(a, b):
    """ Find the largest of two numbers """
    if a >= b:
        return a
    else:
        return b


if __name__ == "__main__":

    a = int(input("Input the fisrt number: "))
    b = int(input("Input the second number: "))
    
    l = largest(a, b)
    print(f"The docstring is: {largest.__doc__}")
    print(f"The largest of two numbers is: {l}")
