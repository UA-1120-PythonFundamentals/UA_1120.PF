# Practical Task 03.1

number = input("Input 4-digit number: ")

# Part 01
res = 1
for n in str(number):
    res *= int(n)
print(f'The product of the digits of this number: {res}')

# Part 02
print(f'The number in reverse order: {str(number)[::-1]}')

# Part 03
res = int(''.join(sorted(str(number))))
print(f'Numbers are sorted in ascending order: {res}')
res = int(str(res)[::-1])
print(f'Numbers are sorted in descending order: {res}')