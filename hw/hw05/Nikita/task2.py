def fibonacci(a):
    x, y = 0, 1
    while x <= a:
        print(x, end = ' ')
        x, y = y, x + y

        
f = int(input('Enter your number: '))
fibonacci(f)
