# isTrue = True
# isFalse = False

# a, b = 5, 10
# print("a == b", a == b)
# print("a != b", a != b)
# print("a > b", a > b)
# print("a < b", a < b)
# print("a >= b", a >= b)
# print("a <= b", a <= b)

# a, b = 10, 10
# print("a >= b", a >= b)
# print("a <= b", a <= b)


# print(1 and "aa" and 0.5 )
# print(1 and "aa" and "test"  )
# print(1 and 0 and 0.5 )
# print([] and 0 and "" )

# print(1 or 0 or 0.5 )
# print([] or 0 or 0.5 )
# print("" or 0 or {} )
# isFalse = [0, False, None, "", [], (), {}, set()]

# a = list()
# print(type(a) is list)

# a = [1,2,3]
# b = a
# c = [1,2,3]
# print(a is b)
# print(a is c)
# print(b is c)
# print(id(a))
# print(id(b))
# print(id(c))
# print(a == b)
# print(a == c)

# # text = "some text"
# d = {"a": 1, "b": 2}
# # l = [4, 5, 6, 7, 8]
# # print("s" in text)
# # print("tex" in text)
# # print("te1" in text)
# print("a" in d)
# print(2 in d)

# print(1 in l)
# print(4 in l)
# print([4, 5] in l)
# l = [4, 5, 6, 7, 8, [4, 5]]
# print([4, 5] in l)

# x = int(input("x: "))
# if x < 10:
#     print(f"{x} < 10")

# print(f"{x=}")


# x = int(input("x: "))
# if x < 10:
#     print("start if")
#     print(f"{x} < 10")
#     print("end if")

# print(f"{x=}")
# temperature = float(input('What is the temperature? ') )
# if temperature > 30:
#     print("start if")
#     print('Wear shorts.', temperature)
#     print("end if")
# else:
#     print("start else")
#     print('Wear long pants.', temperature)
#     print("end else")

# print('Get some exercise outside.')

# age = int(input("age: "))

# if age < 12:
#     print('kid')
# else:
#     if age < 18:
#         print('teenager')
#     else:
#         if age < 50:
#             print('adult')
#         else:
#             print('you are not old')

# if age < 12:
#     print('kid')
# elif age < 18:
#     print('teenager')
# elif age < 50:
#     print('adult')
# else:
#     print('you are not old')

# if age < 12:
#     print('kid')
# elif age < 18:
#     print('teenager')
# elif age < 50:
#     print('adult')
# else:
#     print('you are not old')


# age = int(input("age: "))

# t = "yong" if age < 40 else 'you are not old'
# #t = age < 40 ? "yong"  : 'you are not old'
# status = int(input("http status code: "))
# match status:
#     case 400:
#         print("Bad request")
#     case 401:
#         print("Unauthorized")
#     case 403:
#         print("Forbidden")

#     case 405 | 406 | 407 as error_code:
#         print(f"error {error_code}")
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")
# values = ("load", "http://")
# match values:
#     case "load", link:
#         print(f"load({link})")
#     case "save", link, filename:
#         print(f"save({link}, {filename})")
#     case "save", link, *filenames:
#         for filename in filenames:
#             print(f"save({link}, {filename})")
#     case _:
#         print(f"default({values})")

# values = ("save", "http://", "file")
# match values:
#     case "load", link:
#         print(f"load({link})")
#     case "save", link, filename:
#         print(f"save({link}, {filename})")
#     case "save", link, *filenames:
#         for filename in filenames:
#             print(f"save({link}, {filename})")
#     case _:
#         print(f"default({values})")

# values = ("save", "http://", "file1", "file2","file3")
# match values:
#     case "load", link:
#         print(f"load({link})")
#     case "save", link, filename:
#         print(f"save({link}, {filename})")
#     case "save", link, *filenames:
#         print(f"{filenames}")
#         for filename in filenames:
#             print(f"save({link}, {filename})")
#     case _:
#         print(f"default({values})")


# values = ("save", "http://", ["file1", "file2","file3"])
# match values:
#     case "load", link:
#         print(f"load({link})")
#     case "save", link, filename:
#         print(f"save({link}, {filename})")
#     case "save", link, *filenames:
#         print(f"{filenames}")
#         for filename in filenames:
#             print(f"save({link}, {filename})")
#     case _:
#         print(f"default({values})")


item = ["evening", 51]
match item:
    case ['evening', action] if action >50:
        print(f'You almost finished the day! Now {action}!!!!!!')
    case ['evening', action]:
        print(f'You almost finished the day! Now {action}!')
    case [time, action]:
        print(f'Good {time}! It is time to {action}!')
    case _:
        print('The time is invalid.')