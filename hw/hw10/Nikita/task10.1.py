class Polygon:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class rectangle(Polygon):
    def rectangle(self):
        return self.a * self.b
a = rectangle(10, 20)
b = a.rectangle()
print(b)

        
    