from math import pi
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = 4*pi * self.radius**3 / 3
        self.surface = 4*pi* self.radius**2
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round(self.volume,5)
    def get_surface_area(self):
        return round(self.surface,5)
    def get_density(self):
        return round(self.mass/self.volume, 5)