import random

number = random.randint(1, 100)
for i in range(1, 11):
  print('Guess the number between 1 and 100  ')
  number1 = int(input())
  if number1 == number:
    print('You guessed it in', i, 'attempts.')
    break
  elif number1 <= 0 or number1 > 100:
    print('The choice is out of bounds')
  elif 1 < number1 < number:
    print('Too few')
  else:
    print('Too much')
else:
  print("You didn't guess the number", number)
  