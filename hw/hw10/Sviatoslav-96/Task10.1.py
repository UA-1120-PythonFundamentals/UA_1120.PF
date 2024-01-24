class Polygon():
  def __init__(self, sides):
      self.sides = sides

class Rectangle(Polygon):
  def __init__(self, width, height):
      super().__init__([width, height])
      self.width = width
      self.height = height

  def square(self):
      return self.width * self.height

rectangle = Rectangle(3, 4)

print(rectangle.square())