# def f():
#     # """\tsome text"""
#     print("start run")
#     print("runing")
#     print("stop run")

# f()
# f()
# f()
# print(f.__doc__)
# help(f)
# print(print.__doc__)


# help(print)
# def greet(name):
#     """This function greets to
#     the person passed in as
#     parameter"""
#     text = "Hello, " + name + ". Good morning!"
#     print(text)
#     return text


# # How to call a function in python?
# result = greet("Volodymyr")
# greet("Liubov")
# print(result)


# def my_sum(a, b):
#     if a > b:
#         return a + b
#     elif a < b:
#         return a * b
#     return a, b, a, a, b, b, a


# print(my_sum)
# print(my_sum(1, 2))
# print(my_sum(3, 2))
# print(my_sum(5, 5))


# def f(a):
#     print(f"{a=}")


# # f()
# f("abab")
# # f("abab", 2)


# def f(a, b):
#     ff = 1
#     print(dir())
#     print(f"{a=} {b=}")


# f("abab", 2)
# f(2, "abab")
# # print(a)
# print(dir())


# def print_info(name, age=18):
#     print("Name: ", name)
#     print("Age: ", age)
# # print_info()
# print_info("Andii")
# print_info("Olha", 22)
# print_info("Ostap")
# print_info("Andiy", 55)

# def f(a=1, c=2, b=3, d="test"):
#     print(a,b,c,d)
# f()
# f("d", "f")
# def f(a, c, b=1, d="test"):
#     pass
# def f(l=[]):
#     l.append(1)
#     print(l)
# # f([1,2,3])
# # f([10,20,30])
# f() #[1]
# f() #[1]
# f([1,2,3]) #[1,2,3,1]
# f() #[1]
# def f(a,b):
#     a+=1
#     b+=[1]
#     print(a, b)
# aa = 1
# bb = [1]
# f(aa, bb)
# print(aa, bb)

# def print_info(name, age=18):
#     print("Name: ", name)
#     print("Age: ", age)

# print_info(age=22, name="Olha")

# print_info("AAA", age=22)

# print(1,2,3,4,5, end="@@@", sep="=>")


# def f(*args, **kwarg):
#     print(f"{args=} {kwarg=}")

# f(1,2,3,4,5,76,8,6,5,6,7,8, age=22, name="Olha", a=999)

# def f(a, b, *args, name="A", age=25, **kwarg):
#     print(f"{a=} {b=} {args=} {name=} {age=} {kwarg=}")

# f(1,2,3,4,5,76,8,6,5,6,7,8, age=22, name="Olha", aa=999)


# def f(a, b,  name="A", age=25, *args, **kwarg):#error
#     print(f"{a=} {b=} {args=} {name=} {age=} {kwarg=}")

# f(1,2,3,4,5,76,8,6,5,6,7,8, age=22, name="Olha", aa=999)


# def f(a, b, *args, name="A", age=25, **kwarg):
#     print(f"{a=} {b=} {args=} {name=} {age=} {kwarg=}")


# f(1, 2, 3, 4, 5, 76, 8, 6, 5, 6, 7, 8, age=22, name="Olha", aa=999)

# l = (11, 22, 33, 44, 55, 66)
# f(l[0], l[1], l[2], l[3], l[4], l[5])
# f(*l)
# d = {"a": 1000, "b": 8888, "name": "Liubomyr", "port": "8080"}
# f(*d)
# f(**d)

# # data = {"arg1": request.form}
# f(**f)

# x = 10


# def f():
#     x = 20
#     print(locals())


# print(locals())
# f()
# print(locals())

# x = 10
# def f():
#     print(x)

# f()

# x = 10
# def f():
#     # print(x)
#     x= 20
#     print(x)
# f()
# print(x)

# x = 10
# def f():
#     global x
#     print(x)
#     x= 20
#     print(x)
# f()
# print(x)

# x = 10
# def f():
#     def g():
#         def k():
#             global x
#             print(x)
#             x= 20
#             print(x)
#         k()
#     g()
# f()
# print(x)
# local = "global"
# def outer():
#     local = "local"
#     def inner():
#         global local
#         print("inner => ", local)
#     inner()
#     print("outer => ", local)

# outer()

# print("global =>", local)

# local = "global"

# def outer():
#     local = "local"
#     def inner():
#         nonlocal local
#         print("inner => ", local)
#         local = "inner"
#     inner()
#     print("outer => ", local)

# outer()

# print("global =>", local)
# print("="*30)

# def fuc(n, text=""):
#     if n==1:
#         return 1
#     t = f"{n}*fuc({n-1})"
#     t = f"{text[:-6]}{t}"
#     # print(t)
#     return n*fuc(n-1, t)

# # print(fuc(1000))
# import sys
# sys.setrecursionlimit(1500)
# print(fuc(1400))
# print(fuc(1500))


# def my_sum(a, b):
#     return a+b

# my_f = lambda a, b: a+b

# print(my_sum(10,20))
# print(my_f(10,20))

# l = [1,2,3,4, "12", "-3", "5"]
# def f(a):
#     return int(a)
# l.sort(key=f)
# print(l)
# l.sort(key=lambda e: -int(e))
# print(l)
# def f():
#     return
# print(f())
l = [1,2,3,4,5]
print(sum(l))
s = sum
def sum(a):
    text = ""
    for i in a:
        text += str(i)
    return text
print(sum(l))
print(s(l))
sum = s
print(sum(l))

