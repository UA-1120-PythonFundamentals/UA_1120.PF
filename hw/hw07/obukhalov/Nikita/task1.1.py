
def func (x, y):
    '''Find the largest number'''
    if x >= y:
        return x
    else:
        return y

n = str(input('Enter the first number: '))
n_1 = str(input('Enter the second number: '))
c = func(n, n_1)

print(func.__doc__)
print('The largest is: ',c)
