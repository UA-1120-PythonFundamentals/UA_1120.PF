import math


def circle_area(radius):
    """
        Calculate the area of a circle.

        Parameters:
            - radius (float): Radius of the circle.

        Returns:
            - float: Area of the circle.
    """
    area_c = math.pi * math.pow(float(radius),2)
    return area_c