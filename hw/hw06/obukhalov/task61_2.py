#!/usr/bin/env python


def main():
    while True:
        login = input("Login: ")

        if login.lower() == "first":
            print(f"Hello {login}!")
            break
        else:
            print("Login error! Try again!")
            continue


if __name__ == "__main__":
    main()
