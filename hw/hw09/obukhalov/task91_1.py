#!/usr/bin/env python


import random


def game():
    number = random.randint(1, 100)

    print("Guess the number from 1 to 100.\n\n")

    counter = 0

    while counter < 10:
        guess = int(input("Enter the number: "))

        if guess == number:
            print("Congratulation! You won!")
            return None

        counter += 1

    print("Sorry. You lost.")
    return None


if __name__ == "__main__":
    game()
