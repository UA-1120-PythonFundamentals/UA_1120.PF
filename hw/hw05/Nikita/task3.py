def factorial(x):
    a = 1
    for i in range(2, x + 1):
        a = a * i
    
    return a
    

c = int(input('Enter your number: '))
print(factorial(c))
