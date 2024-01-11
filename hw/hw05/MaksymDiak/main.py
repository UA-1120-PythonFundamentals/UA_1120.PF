
# -- Task 1 --
l = [1, 5, 10, 13, 14]

for i in range(0, len(l)):
    l[i] = float(l[i])
print(l)


# -- Task 2 --
n = int(input("Enter n: "))
fib = [0, 1]

if n <= 0:
    print('Error!')
else:
    while fib[-1] + fib[-2] <= n:
            fib.append(fib[-1] + fib[-2])
    print(fib)


# -- Task 3 --
num = int(input('Enter a number: '))
factorial = 1    

if num < 0:    
    print(f'!{num} doesn\'t exist')       
else:    
    for i in range(1, num+1):    
        factorial = factorial * i    
    print(f'!{num} = {factorial}')
