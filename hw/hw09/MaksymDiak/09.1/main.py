import random


def gess(attempts=10):
    n = random.randint(1, 100)
    print(f"\nYou have {attempts} attempts to gess the number!", end="\n\n")
    for i in range(attempts):
        print(f"\tAttempt {i+1}:")
        x = int(input("Input number: "))
        if x < n:
            print("Your number is less than the guessed number!")
        elif x > n:
            print("Your number is greater than the guessed number!")
        else:
            return "You have guessed the number!"
    return "You didn't guess the number!"


print(gess())
