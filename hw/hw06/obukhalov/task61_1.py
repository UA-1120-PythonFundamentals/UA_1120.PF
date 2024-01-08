#!/usr/bin/env python


def main():
    even_l = []
    odd_l = []
    other_l = []

    for i in range(1, 11):
        if i % 2 == 0:
            even_l.append(i)
        elif i % 3 == 0:
            odd_l.append(i)
        else:
            other_l.append(i)

    print(f"Even numbers are: {' '.join(map(str, even_l))}")
    print(f"Odd numbers are: {' '.join(map(str,odd_l))}")
    print(f"Other numbers are: {' '.join(map(str, other_l))}")


if __name__ == "__main__":
    main()
