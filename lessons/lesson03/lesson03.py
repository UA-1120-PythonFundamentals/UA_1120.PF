# a = 1
# print(type(a), a)
# a = "1"
# print(type(a), a)
# a = (1,)
# print(type(a), a)
# a = 1.3
# print(type(a), a)

# a = "test"
# print(id(a))
# a = "test3"
# print(id(a))
# l = []
# print(id(l))
# l.append(1)
# print(id(l))
# l.append(1)
# l.append("1")
# l.append((1,2,3,))
# l.append({1:"2"})
# print(l)

# a = 1.3
# print(type(a) is float)
# print(type(a) is int)
# print(isinstance(a, float))
# print(isinstance(a, int))

# class A:pass
# class B(A):pass
# a = A()
# b = B()
# print(type(a) is A)
# print(type(b) is A)
# print(isinstance(a, A))
# print(isinstance(b, A))


# a = 1 + 2 + 3 \
#     + 4 + 5 + 6
# a = (1 + 2 + 3
#     + 4 + 5 + 6)


# a, b, c = 1,2,3
# print(a, b, c)
# l  = ["first", 2, 3.0]
# a, b, c = l
# print(a, b, c)

# a=b=c=1
# print(a, b, c)

# a = 1
# b = a
# c = a
# print(a, b, c)
# a = 1
# b = 2
# c = a
# print(a, b, c)

# a = [1,2,3,4]
# b = a
# c = a
# print(a, b, c)
# a[0] = 10
# b[1] = 20
# c[2] = 30
# print(a, b, c)
# PI = 3.14
# print(PI)
# PI = 33.14
# print(PI)


# f = 1.1
# f = 1e-2
# print(f)
# f = 1e2
# print(f)


# i = 10
# print(i)
# i = i**9999
# import sys
# sys.set_int_max_str_digits(10000)

# print(i)

# i = 0b10
# print(i)
# i = 0o10
# print(i)
# i = 0x10
# print(i)

# a = True
# b = False

# print(a, b)
# print(a +10, b+10)

# a = None #nill
# print(a)

# l = [1,2,3,1,2,3]
# l[1] = 10
# print(l)
# l = (1,2,3)
# l[1] = 10 #error
# print(l)


# s = {1,2,3,4,5,6,1,2,3,5432,34,5,6,6,43,23,2,43,54}
# print(s)

# d = {
#     "key": "value",
#     1:2,
#     "15": lambda : 10*5
# }
# print(d)
# print(d[1])
# print(d["15"])
# print(d["15"]())
# # print(d["11"])#error

# print(int("1512113"))
# print(int("1000"))
# print(int("1000", 2))
# print(int("1000", 36), int("zz", 36))

# obj = 35
# print(str(obj))
# a = eval("33+59")
# print(a)

# for i in range(100):
#     print(f"{i} - {chr(i)}")
# for i in "range(100)":
#     print(f"{i} - {ord(i)}")

# i = 21
# print(bin(i))
# print(oct(i))
# print(i)
# print(hex(i))
# print("Hello!\n Wiki!")
# print('Hello!\n Wiki!')
# a = ('Hello!' 
#      '\n Wiki!')
# a = """aaa
# bbb
# ccc
# """
# print(a)

# # This prints out "John is 23 years old. Your sallary is 999.990 $"
# name = "John"
# age = 23
# salary = 999.99
# template = "%s is %d years old. Your sallary is %.3f $"
# print(template % (name, age, salary))
# print(template % ("Liubomyr", 37, 123.12399))

# template = "{} is {} years old. Your sallary is {:.3f} $"
# print(template.format(name, age, salary))

# template = "{n} is {a} years old. Your sallary is {s}, {n} $"
# print(template.format(a=age, n=name, s=salary))

# print(f"{name} is {age} years old. Your sallary is {salary*33} $")

# st = "programiz"
# print(st[0], st[1], "...", st[len(st)-1])
# print(st[0], st[1], "...", st[-1])
# # print(st[1220])#errro
# print(st[1:5])
# print(st[1:5:2])
# print(st[:5])
# print(st[2:])
# print(st[:])

# st = "oNvERT tExT to rANDOm CaSe letTeRS."
# print(st.lower())
# print(st.upper())
# print(st.split("e"))
# print("e".join(['oNvERT tExT to rANDOm CaS', ' l', 'tT', 'RS.']))

print(3**3)
print(9**0.5)
print((3)**(0.2))