#!/usr/bin/env python


class Polygon:

    def __init__(self):
        self.area = 0

    def area_calc(self):
        pass

class Rectangle(Polygon):

    def __init__(self):
        super().__init__()

    def area_calc(self, a, b):
        self.area = a * b
        return self.area

if __name__ == "__main__":

    rect = Rectangle()

    a = int(input("Rectangle side A :"))
    b = int(input("Rectangle side B :"))
    area = rect.area_calc(a, b)

    print(f"The ractangle area is: {area}")


