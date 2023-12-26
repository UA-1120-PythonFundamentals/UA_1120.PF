#!/usr/bin/env python

#import this
#import codecs


def task31_part1():
    py_ph_s = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
    print("\n\n", "*"*20, " PART1 ", "*"*20, "\n\n")
    py_ph_l = py_ph_s.split("\n")
    while True:
        try:
            i = int(input(f"Input line number from 1 to {len(py_ph_l) - 2}: "))
        except ValueError:
            print("Input error. Only numbers in range from 1 to {len(py_ph_l) - 2} accepteble.\nTry again.")
            continue
        if i < 1 or i > (len(py_ph_l) - 2):
            print("Input error. Only numbers in range from 1 to {len(py_ph_l) - 2} accepteble.\nTry again.")
            continue
        break

    better_count = py_ph_l[i].count("better")
    never_count = py_ph_l[i].count("never")
    is_count = py_ph_l[i].count("is")
    print(f"Line:\n{py_ph_l[i]}\nBetter occurence: {better_count}\nNever occurence: {never_count}\nIs occurence: {is_count}")
    print(f"\n\n\nPython Phylosophy in upper case:\n{py_ph_s.upper()}")
    print(f"\n\n\nReplace i with &:\n{py_ph_s.replace('i','&')}")


def task31_part2():

    while True:
        n = input(f"Input four digit number: ")
        if not n.isdigit():
            print("Input error. You can only enter the digits. Try again.")
            continue
        if len(n) != 4:
            print("The number must be exactly four digits. Try again.")
            continue
        break
   
    print("\n\n", "*"*20," PART2 ","*"*20,"\n\n")
    product = int(n[0]) * int(n[1]) * int(n[2]) * int(n[3])
    print(f"The four digits product of {n} is: {product}")
    print(f"The reverse order of {n} is: {n[::-1]}")
    print(f"The number {n} sorted in ascendig order is: {''.join(sorted(n))}")


def task31_part3():
    print("\n\n", "*"*20," PART3 ","*"*20,"\n\n")
    a = input("Enter value for variable a: ")
    b = input("Enter value for variable b: ")

    a,b = b,a

    print(f"Swapped values of a and b are: {a} and {b}")

def main():
    task31_part1()
    task31_part2()
    task31_part3()


if __name__ == "__main__":
    main()
