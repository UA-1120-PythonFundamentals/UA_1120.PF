class polygon:
    def __init__(self, a , b):
        self.a = a
        self.b = b
        
class rectangle(polygon):
    def rect(self):
       return  self.a * self.b
a=rectangle(10,5)
b=a.rect()
print(b)

