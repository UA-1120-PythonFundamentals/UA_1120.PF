
# -- Task 1 --
l = [[], [], []]

for i in range(1, 11):
    if i % 2 == 0:
        l[0].append(i)
    elif i % 3 == 0:
        l[1].append(i)
    else:
        l[2].append(i)

print(f'Even numbers that are divisible by 2: {l[0]}')
print(f'Odd numbers, which are divisible by 3: {l[1]}')
print(f'Numbers that are not divisible by 2 and 3: {l[2]}')


# -- Task 2 --
while True:
    login = input('Input login: ')
    if login == "First":
        print(f'Hi, {login}!')
        break
    else:
        print('Error! Try to input another login!')
        continue
