#!/usr/bin/env pyton


def main():
    # User input
    while True:
        try:
            n = int(input("Input decimal number: "))
        except ValueError:
            print("Input error! Only decimal number are allowed. Try again.")
            continue

        if n < 0:
            print("Input error! Only positive decimal number are allowed. Try again.")
            continue

        break

    # Basic cases
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    # Calculate factorial
    factorial = n

    while n > 1:
        factorial *= n - 1
        n -= 1

    return factorial


if __name__ == "__main__":
    f = main()
    print(f)
