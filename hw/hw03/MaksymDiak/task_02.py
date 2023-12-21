
number = 7649

# -- 1 --
res = 1
for i in str(number):
    res *= int(i)

print(f'task_1: {res}')

# -- 2 --
print(f'task_2: {str(number)[::-1]}')

# -- 3 --
d = [int(el) for el in str(number)]
res = ''.join(map(str, sorted(d)))
print(f'task_3: {res}')
