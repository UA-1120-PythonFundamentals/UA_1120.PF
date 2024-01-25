import math
class Sphere:
    def init(self, radius,mass):
        self.radius = radius
        self.mass = mass
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        self.volume = (4/3)* math.pi*self.radius**3
        return round(self.volume,5)
    def get_surface_area(self):
        return round((4*math.pi*self.radius**2),5)
    def get_density(self):
        return round(self.mass / self.volume,5)