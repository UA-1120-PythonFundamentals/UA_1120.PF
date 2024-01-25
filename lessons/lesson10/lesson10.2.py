# class Point:
#     def __init__(self, x=0, y=0):
#         print("__init__Point")
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"X:{self.x} Y:{self.y}"

#     def __repr__(self):
#         print("__repr__Point")
#         return f"({self.x}, {self.y})"

#     def __add__(self, other):
#         point = Point()
#         point.x = self.x + other.x
#         point.y = self.y + other.y
#         return point

#     def __lt__(self, other):
#         return self.x > other.x
#     def __bool__(self):
#         return not self.x == self.y == 0


# class Point3D(Point):
#     def __init__(self, x=0, y=0, z=0):
#         print("__init__Point3D")
#         super().__init__(x, y)
#         self.z =  z

#     def __repr__(self):
#         print("__repr__Point3d")
#         return f"({self.x}, {self.y}, {self.z})"

#     def __add__(self, other):
#         point = Point3D()
#         point.x = self.x + other.x
#         point.y = self.y + other.y
#         point.z = self.z + (other.z if type(other) is Point3D else 0)
#         return point

#     def __str__(self):
#         return f"X:{self.x} Y:{self.y} Z:{self.z}"


# p1 = Point3D(1, 22,1)
# p2 = Point(3, -19)
# p3 = Point(-11, 5)
# points = [p1, p2, p3, Point3D(-1, -1,10)]

# print(points)

# p4 = p1 + p2
# print(p4, type(p4))

# class A:
#     pass
# class B(A):
#     def print(self):print("B")
# class C(A):
#     def print(self):print("C")
# class D(B, C):
#     pass
# class E(D):
#     pass
# class F(C):
#     pass
# class G(F,E):
#     pass

# g = G()
# g.print()

# print(G.__mro__)


# class A:
#     def print(self):
#         print(self, type(self))

#     @classmethod
#     def print_cls(cls):
#         print(cls, type(cls))

#     @staticmethod
#     def print_static():
#         print("static")

# a = A()
# a.print()
# # A.print()
# a.print_cls()
# A.print_cls()
# a.print_static()
# A.print_static()

# class A:
#     def __init__(self,x,y,z) -> None:
#         self.x = x
#         self._x = y
#         self.__x = z

#     def __str__(self) -> str:
#         return f"{self.x=} {self._x=} {self.__x=}"

#     def calc(self):
#         return self.x+self._x+ self.__x + self.__calc()

#     def __calc(self):
#         return self.x+self._x+ self.__x

# a = A(2,4,6)
# print(a)
# print(a.x)
# print(a._x)
# # print(a.__x)
# print(a.calc())
# print(a._A__x)
# print(a._A__calc())


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"X:{self.__x} Y:{self.__y}"

    def __repr__(self):
        return f"({self.__x}, {self.__y})"

    def get_x(self):
        print(f"get_x:{self.__x}")
        return self.__x

    def set_x(self, x):
        print(f"set_x:{self.__x}", end=" -> ")
        self.__x = x
        print(f"{self.__x}")

    x = property(get_x, set_x)

    @property
    def y(self):
        print(f"get_y:{self.__y}")
        return self.__y

    @y.setter
    def y(self, y):
        print(f"set_y:{self.__y}", end=" -> ")
        self.__y = y
        print(f"{self.__y}")

    def print(self):
        print(f"X:", self.__x)
        print(f"Y:", self.__y)


p = Point(12, 18)
print(p)
# print(p.x)
# print(p.get_x())
# p.set_x(55)
# print(p.get_x())
print(p.x)
p.x = 99
print(p)
print(p.y)
p.y = -22
print(p)
p.print()


class Point2D(Point):
    def print(self):
        print(f"X -> ", self.x)
        print(f"Y -> ", self.y)

    def print(self, text="GGG"):
        print(text)
        print(f"X -> ", self.x)
        print(f"Y -> ", self.y)


p = Point2D()
p.print()
