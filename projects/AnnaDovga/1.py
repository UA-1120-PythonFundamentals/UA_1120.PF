def is_valid(num, x, y):
    num = num.strip()
    while True:
        if num.isdigit():
            num = int(num)
            if x <= num <= y:
                return num
            else:
                num = input(f'Enter an integer from {x} to {y}: ')
        else:
            num = input(f'Pleasе, enter an integer from {x} to {y}: ')


def is_valid_ans(ans):
    variants = ['yes', 'no']
    ans = ans.strip()
    if ans.lower() in variants:
        return True


def generate_chars(chars, symbols, quests, counter):
    while True:
        for i in range(len(quests)):
            ans = input(f'{quests[i]} ')
            while not is_valid_ans(ans):
                ans = input('Please write yes/no ')
            if ans == 'yes':
                chars.append(symbols[i])
                counter += 1
            if i == 3 and counter < 1:
                print('\nPlease, select the groups of characters that make up the password')
                break
            if i == 4:
                if ans == 'yes':
                    chars = ' '.join(chars)
                    ambiguous = symbols[i]
                    for j in ambiguous:
                        if j in chars:
                            chars = chars.replace(j, '')
                    chars = chars.split()
        if len(chars) > 0:
            return chars
            break


def generate_password(length, chars):
    import random
    result = ''
    second_time = 0
    while len(result) < length:
        if second_time > 0:
            random.shuffle(chars)
        for c in range(len(chars)):
            result += random.choice(chars[c])
            if len(result) == length:
                break
        second_time += 1
    return str(result)


import random

symbols = ['0123456789',
           'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
           'abcdefghijklmnopqrstuvwxyz',
           '!$%&*+-=?@^_',
           'il1Lo0O']
quests = ['Include numbers 0123456789?',
          'Include capital letters ABCDEFGHIJKLMNOPQRSTUVWXYZ?',
          'Include lowercase letters abcdefghijklmnopqrstuvwxyz?',
          'Include characters !#$%&*+-=?@^_?',
          'Exclude ambiguous characters il1Lo0O?']
counter = 0
chars = []
passwords = []

print('\n    C R E A T E   P A S S W O R D S')

while True:
    quantity = input('\n How many passwords should create? We can create up to 100 ')
    quantity = int(is_valid(quantity, 1, 100))

    length = input('How long is the password needed? Allowed length from 4 to 20 characters ')
    length = int(is_valid(length, 4, 20))

    print('\nAnswer please yes/no')

    chars = generate_chars(chars, symbols, quests, counter)

    for k in range(quantity):
        password = list(generate_password(length, chars))
        password = random.sample(password, length)
        while ''.join(password) in passwords:
            password = list(generate_password(length, chars))
            password = random.sample(password, length)
        passwords.append(''.join(password))
    print()
    print(*passwords, sep='\n')

    again = input('\nDo you want to create some more passwords? ')
    while not is_valid_ans(again):
        again = input('Input yes/no ')
    if again.strip() == 'yes':
        counter = 0
        chars = []
        passwords = []
        continue
    else:
        break
