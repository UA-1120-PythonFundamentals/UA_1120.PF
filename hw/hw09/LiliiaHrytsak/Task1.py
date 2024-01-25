from random import randint


def guess_number():
    # Generate a random number between 1 and 100
    target_number = randint(1, 100)

    max_attempts = 10
    attempts = 0

    while True:
        # Increment the number of attempts
        attempts += 1

        # Get user input for the guessed number
        guess = int(input("Guess a number in the range from 1 to 100: "))

        # Check if the guess is too low, too high, or correct
        if guess < target_number:
            print("Number too low")
        elif guess > target_number:
            print("Number too high")
        else:
            print(f"Exactly right! You did it in {attempts} tries")
            break  # Exit the loop if the guess is correct

        # Check if the maximum number of attempts is reached
        if attempts == max_attempts:
            print("Game over! Unfortunately, you used all your chances.")
            break


if __name__ == "__main__":
    guess_number()