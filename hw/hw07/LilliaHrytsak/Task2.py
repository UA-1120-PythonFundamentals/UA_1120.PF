import math


def triangle_area(base, height):
    """
        Calculate the area of a triangle.

        Parameters:
            - base (float): Length of the base of the triangle.
            - height (float): Height of the triangle.

        Returns:
            - float: Area of the triangle.
    """

    area_t = 0.5 * float(base) * float(height)
    return area_t


def rectangle_area(length, width):
    """
        Calculate the area of a rectangle.

        Parameters:
            - length (float): Length of the rectangle.
            - width (float): Width of the rectangle.

        Returns:
            - float: Area of the rectangle.
    """
    area_r = float(length) * float(width)
    return area_r


def circle_area(radius):
    """
        Calculate the area of a circle.

        Parameters:
            - radius (float): Radius of the circle.

        Returns:
            - float: Area of the circle.
    """
    area_c = math.pi * float(radius) ** 2
    return area_c


input_value = input('Which area do you want to calculate: rectangle, triangle, or circle? ')
if input_value not in ['rectangle', 'triangle', 'circle']:
    print("Notvalid input")
else:
    if input_value == 'rectangle':
        area = rectangle_area(length=input("Write the length "), width=input("Write the width "))
    elif input_value == 'triangle':
        area = triangle_area(base=input("Write the base "), height=input("Write the height "))
    elif input_value == 'circle':
        area = circle_area(radius=input('Write radius '))
    print(f'Chosen area of {input_value} = {area}')
