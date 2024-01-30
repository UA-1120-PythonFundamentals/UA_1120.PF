class Polynom():
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polynom):
    def __init__(self, width, height):
        super().__init__([width, height])
        self.width = width
        self.height = height

    def find_area(self):
        return self.width * self.height


r = Rectangle(2, 5)
print(r.find_area())
