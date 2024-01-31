# l = [x**x for x in range(10)]
# print(l)

# l = [x**x for x in range(10) if x % 2]
# print(l)


# l = [(x, y) for x in range(10) for y in range(x)]
# # for x in range(10):
# #     for y in range(x):
# #         (x, y)
# print(l)
# t = l[0]
# for e in l:
#     if e[0] != t[0]:
#         print()
#         t = e
#     print(e, end=" ")
# print()

# text = "bsdjbvjsdhbvuhsnavbdfi"
# s = {s for s in text if text.count(s) > 2}
# print(s)

# d = {s: text.count(s) for s in text}
# print(d)


# t = ((x, y) for x in range(10) for y in range(x))
# print(t)
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))

# # while t:
# #     print(next(t))

# for i in t:
#     print(i)

# t = ((x, y) for x in range(10) for y in range(x))
# for i in t:
#     print(i)

# from functools import reduce
# def a_add_b(a, b):
#     print(f"{a}+{b}={a+b}")
#     return a+b
# print(reduce(a_add_b, [47,11,42,13]))
# print(reduce(a_add_b, [47,11,42,13], -22))


# list_number = [25, 739, 48]
# # print(next(list_number))
# custom_iterator = iter(list_number)
# print(next(custom_iterator))
# print(next(custom_iterator))
# print(next(custom_iterator))
# # print(next(custom_iterator))

# def my_for(itr, fun):
#     custom_iterator = iter(itr)
#     while True:
#         try:
#             x = next(custom_iterator)
#             fun(x)
#         except StopIteration:
#             break


# def my_f(x):
#     print(x)

# my_for([1,2,3,4], my_f)
# my_for(range(10,15), my_f)
# my_for((i for i in range(100, 105)), my_f)


class MyNumbers:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        print("__iter__")
        self.a = 1
        return self

    def __next__(self):
        print("__next__")
        if self.a <= self.max:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


# x = MyNumbers(5)
# for i in x:
#     print(i)
# N = 10
# print(f"{N=}")
# i = [MyNumbers(i) for i in range(N)]
# g = (MyNumbers(i) for i in range(N))
# print(i.__sizeof__())
# print(g.__sizeof__())
# N = 100
# print(f"{N=}")
# i = [MyNumbers(i) for i in range(N)]
# g = (MyNumbers(i) for i in range(N))
# print(i.__sizeof__())
# print(g.__sizeof__())
# N = 1000
# print(f"{N=}")
# i = [MyNumbers(i) for i in range(N)]
# g = (MyNumbers(i) for i in range(N))
# print(i.__sizeof__())
# print(g.__sizeof__())
# N = 10000
# print(f"{N=}")
# i = [MyNumbers(i) for i in range(N)]
# g = (MyNumbers(i) for i in range(N))
# print(i.__sizeof__())
# print(g.__sizeof__())

# def my_generator(N):
#     print("my_generator")
#     yield 10
#     yield 20
#     yield 30

# print(type(my_generator))

# g = my_generator(20)
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def my_generator(N=5):
#     print("generator start")
#     i = 0
#     while i < N:
#         print(f"returned {i=}")
#         yield ("i=", i)
#         print(f"i += {1} ", end=" => ")
#         i += 1
#         print(f"next {i=}")
#     print("generator end")

# # g = my_generator(30)
# # print("*"*10)
# # print(next(g))
# # print("*"*10)
# # print(next(g))
# # print("*"*10)
# # print(next(g))
# # print("*"*10)
# # print(next(g))
# # print("*"*10)
# # print(next(g))
# # print("*"*10)
# # print(next(g))

# g = my_generator(10)
# for i in g:
#     pass


# def my_decorator(fun):
#     print("my_decorator")
#     print("id(fun)", id(fun), fun.__name__)
#     def wraper(*args, **qwargs):
#         print("*"*10)
#         result = fun(*args, **qwargs)
#         print("*"*10)
#     print("id(wraper)", id(wraper), wraper.__name__)
#     return wraper


# @my_decorator
# def f(text, n):
#     print(text*n)

# print("id(f)",id(f), f.__name__)
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# f("aa", 7)
# f("text", 5)

# @my_decorator
# def f2(l):
#     print(list(l))

# f2(range(10))

# f("text", 5)

# @f2
# def ff():
#     pass


def my_decorator(sep, rep=5):
    def inner(fun):
        print("my_decorator")

        def wraper(*args, **qwargs):
            print(sep * rep)
            result = fun(*args, **qwargs)
            print(sep * rep)

            return result

        return wraper

    return inner


@my_decorator("><", 10)
def f(text, n):
    print(text * n)


@my_decorator("_+_")
def f2(text, n):
    print(text * n)


f("text", 5)
f2("text", 5)
f("text", 5)
f2("text", 5)


@my_decorator("_+_")
def f3(a, b):
    return a + b


t = f3(1, 6)
print(t)

import time


def timeit(func):
    def wraper(*args, **qwargs):
        start_time = time.perf_counter()
        result = func(*args, **qwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time

        print(f"function{func.__name__} {args} {qwargs} took:{total_time:.8f} seconds")
        return result

    return wraper


@timeit
def factorial1(n):
    result = 1
    for i in range(n + 1):
        result *= i


@timeit
def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n - 1)


factorial1(100)
factorial1(500)
factorial2(100)
# factorial2(500)
