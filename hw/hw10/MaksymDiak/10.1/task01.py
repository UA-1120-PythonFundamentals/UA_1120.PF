class Polygon:
    def __init__(self, n):
        self.n = n
        self.sides = [0 for i in range(n)]


class Rectangle(Polygon):
    def __init__(self, length, width):
        Polygon.__init__(self, 2)
        self.lenth = length
        self.width = width

    def find_sq(self):
        return self.lenth * self.width
