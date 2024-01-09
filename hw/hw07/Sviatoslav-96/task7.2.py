def rectangle_area(width,lenght):
  rectangle_area = width * lenght
  return rectangle_area

result = rectangle_area(5, 10)

print(result)

import math


def triangle_area(a, b, c):
  """
  Parametros:
  A - lenght of the first side
  B - lenght of the second side
  C - lenght of the third side

  S = semiperimeter
  """
  
  s = (a + b + c) / 2
  triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
  return triangle_area

result = triangle_area(5, 7, 10)

print(result)


def circle_area(radius):
   trapezoid_area = math.pi * radius**2
   return trapezoid_area
radius = 5
result = circle_area(radius)

print (result)