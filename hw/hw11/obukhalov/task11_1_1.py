#!/usr/bin/env python


class AgeError(Exception):
    pass


def main():
    age_string = input("Enter your age: ")

    try:
        age_int = int(age_string)
    except ValueError:
        print("Input error! Age must consists only digital numbers")
        return None
        
    if age_int < 0:
        raise AgeError("Error! Age can't be negative!")
    else:
        if age_int % 2 == 1:
            print("Age is odd")
        else:
            print("Age is even")


if __name__ == "__main__":
    main()
