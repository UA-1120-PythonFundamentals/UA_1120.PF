class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"X:{self.x} Y:{self.y}"

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        point = None
        if isinstance(other, Point):
            point = Point()
            point.x = self.x + other.x
            point.y = self.y + other.y
        elif type(other) is int:
            point = Point()
            point.x = self.x + other
            point.y = self.y + other
        return point

    def __lt__(self, other):
        return self.x > other.x

    def __bool__(self):
        return not self.x == self.y == 0
