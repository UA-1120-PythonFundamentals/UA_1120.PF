import random as r

def guess():
    random_number =  r.randint(1, 100)
    attempts = 10
    for i in range(attempts):
        user_guess = int(input('Guess your number from 1  to 100: '))
        if user_guess < random_number:
            print('Your nember higher. ')
        elif user_guess > random_number:
            print('Your number less.')
        elif user_guess == random_number:
            print('My congratulations, you guessed the number! ')
            return
    
    print('Sorry, your attempts are over!')

    
guess()