#!/usr/bin/env pyton


def main():
    fibonacci = []

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
        return "0"
    elif n == 1:
        return "0 1"
    else:
        fibonacci = [0, 1]

    # Calculate fibonacci number until n
    while True:
        n1, n2 = fibonacci[-2:]
        next_n = n1 + n2
        if next_n <= n:
            fibonacci.append(next_n)
        else:
            break

    return " ".join(map(str, fibonacci))


if __name__ == "__main__":
    f = main()
    print(f)
