import math


class Sphere(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_radius(self):
        return self.x

    def get_mass(self):
        return self.y

    def get_volume(self):
        res = 4 / 3 * math.pi * self.x ** 3
        return round(res, 5)

    def get_surface_area(self):
        res = 4 * math.pi * self.x ** 2
        return round(res, 5)

    def get_density(self):
        res = self.y / self.get_volume()
        return round(res, 5)