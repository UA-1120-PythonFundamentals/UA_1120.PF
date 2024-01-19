#/usr/bin/env pyton

import re


def main():
    
    while True:

        password = input("Enter the password: ")

        if len(password) < 6 or len(password) > 16:
            print("The password is not valid! Try again.")
            continue
        match = re.search(r"[a-z]+", password)
        if not match:
            print("The password is not valid! Try again.")
            continue
        match = re.search(r"[A-Z]+", password)
        if not match:
            print("The password is not valid! Try again.")
            continue
        match = re.search(r"[0-9]+", password)
        if not match:
            print("The password is not valid! Try again.")
            continue
        match = re.search(r"[$#@]+", password)
        if not match:
            print("The password is not valid! Try again.")
            continue
                    
        break


if __name__ == "__main__":
    main()
