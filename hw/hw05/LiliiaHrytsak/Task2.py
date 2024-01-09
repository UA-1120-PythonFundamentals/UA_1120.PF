def make_fibo(n):
    n1 = 0
    n2 = 1
    k = 0
    if n == 1:
        print(n1)
    else:
        while k < n:
            print(n1, end=", ")
            nx= n1 + n2
            n1 = n2
            n2 = nx
            k += 1

make_fibo(4)