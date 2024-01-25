#Calculating the factorial of the entered number
n = int(input('Enter a integer number: '))
factorial = 1    
if n < 0:    
    print(f'Sorry, but {n}! doesn\'t exist')       
else:    
    for i in range(1, n+1):    
        factorial *= i    
    print(f'{n}! = {factorial}')