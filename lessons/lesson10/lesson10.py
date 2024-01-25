# list

# a = [1,2,3]
# print(type(list), list)
# print(type(a), a)
# a.append(1)

# class MyClassA:
#     """my class"""
#     pass

# a = MyClassA()
# my_inst = MyClassA()
# print(type(MyClassA), MyClassA)
# print(type(a), a)
# print(type(my_inst), my_inst)


# class myClass:
#     """my class"""
#     cm = [1]
#     ci = 10
#     def __init__(self):
#         print("__init__")
#         self.im = set()
#         self.ii = "test"

# def print_my_class(obj):
#     print(f"{obj.cm} {obj.ci} {obj.im} {obj.ii}")


# obj1 = myClass()
# obj2 = myClass()

# print_my_class(obj1)
# print_my_class(obj2)
# obj1.cm.append(10)
# obj2.im.add(2)
# print_my_class(obj1)
# print_my_class(obj2)
# print(dir(obj1))
# print(dir(myClass))
# print(obj1.__dict__)
# print(myClass.__dict__)
# print(myClass.cm)
# myClass.ci = "new_int"
# print_my_class(obj1)
# print_my_class(obj2)
# myClass.im.append("new_int")


# class User:
#     def __init__(self, name="Ivan", age=18):
#         self.name = name
#         self.age = age

#     def __str__(s):
#         return f"name: {s.name} age: {s.age}"

#     def my_print(self):
#         print(
#             f"""{self.name}
#                 {self.age}"""
#         )


# user1 = User()
# user2 = User("olha", 21)
# users = str(user1) + str(user2)
# print(user1)
# print(user2)
# print(users)
# user1.my_print()
# user2.my_print()
# User.my_print(user1)

# m_p = User.my_print
# print(m_p)
# print(user1.my_print)
# m_p(user1)

# def short_print(obj):
#     print(f"<{obj.name[:2]} {str(obj.age)[:2]}>")

# short_print(user1)
# User.s_print = short_print

# user1.s_print()
# user2.s_print()


# class User:
#     def __init__(self, name="Ivan", age=18):
#         print("__init__", self.__dict__)
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"name: {self.name} age: {self.age}"
#     def __del__(self):
#         print("__del__", self.__dict__)

# user1 = User()
# user2 = User("olha", 21)
# print(user1)
# print(user2)
# # def f():pass
# # user3 =  f
# # User.__init__(user3)
# # print(user3)
# # print(user3.name)
# print(dir())
# del user2
# del user1
# print(dir())
# user3 = User("AAA", 999)
# # print(user2)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"X:{self.x} Y:{self.y}"

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        point = Point()
        point.x = self.x + other.x
        point.y = self.y + other.y
        return point

    def __lt__(self, other):
        return self.x > other.x
    def __bool__(self):
        return not self.x == self.y == 0


p1 = Point(1, 22)
p2 = Point(3, -19)
p3 = Point(-11, 5)
points = [p1, p2, p3, Point(-1, -1)]

print(p1, p2, p3, points)

p4 = p1 + p2
print(p4)
points.sort(key=lambda p: (p.x**2 + p.y**2) ** (0.5))
print(points)
points.sort()
print(points)
print(p1>p2)
print(p1<p2)
print(bool(p1))
p5 = Point()
print(bool(p5))
points.append(p5)
print(points)
for point in points:
    if point:
        print(point)
    else:
        print("is core", point)