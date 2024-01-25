#Print Fibonacci numbers up to the entered number n
x, y = 0, 1
n = int(input("Enter a positive integer number: "))
if n > 0:
    while x <= n:
        print(x, end=" | ")
        x, y = y, x + y
else:
    print('Error: The number is not positive integer')