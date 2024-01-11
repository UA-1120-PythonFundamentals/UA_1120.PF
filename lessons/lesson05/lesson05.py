# start = 0
# while start < 10:
#     print(start)
#     start += 1
# print("out while", start)

# s = "abcdefg"
# while s:
#     print(s)
#     s = s[1:]

# s = "abcdefg"
# while s:
#     s = s[1:]
#     print(s)


# print("out while", s)

# x = int(input("x: "))

# while x > 1:
#     print(x)
#     x = int(input("x: "))
# else:
#     print("else")


# s = "abcdefg"
# for i in s:
#     # print(i, end="=>")
#     print(i)

# s = [1, 2, "adc", [1, 2, 3], 15]
# for i in s:
#     # print(i, end="=>")
#     print(i)
# for i in 15: #error
#     # print(i, end="=>")
#     print(i)
# d = {1:2, 2:3}
# for i in d:
#     # print(i, end="=>")
#     print(i, d[i])

# print(list(range(10)))
# print(range(10))
# print(list(range(3, 15)))
# print(list(range(3, 15, 4)))

# s = input("text: ")
# print("len(s): ", len(s))
# for i in range(len(s)):
#     # print(i, end="=>")
#     print(f"s[{i}]={s[i]}")

# s = [1, 2, "adc", [1, 2, 3], 15]
# for i in range(len(s)):
#     # print(i, end="=>")
#     print(f"s[{i}]={s[i]}")

# for i in range(10):
#     print("begin")
#     print("\t", i)
#     if i == 5:
#         break
#     print("end")5

# else:
#     print("end for")
# print("all end")
# is_run = True
# s = 0
# while is_run:
#     x = int(input("x:"))
#     if x == 0:
#         is_run = False
#     if x < 0:
#         print("Error")
#         break
#     s += x
# else:
#     print("sum=", s)
# print("end")

# l = [1,2,-3,4,-66,25,23]
# s = 0
# for element in l:

#     print(f"sum={s} new_element:{element}")
#     if element <0:
#         continue
#     print(f"sum={s}+{element}")
#     s += element
#     print()
# print(s)
# import random
# count = 0
# real_count = 0
# print(dir())
# while count<10:
#     real_count +=1
#     x = random.randint(-10, 20)
#     print(f"{x=}", end="\t=>\t")
#     if x % 2:
#         print("go next number")
#         continue
#     print(x**x)
#     count += 1

# print(f"{count=}")
# print(f"{real_count=}")
# print(x)
# print(dir())
for i in range(20):
    pass