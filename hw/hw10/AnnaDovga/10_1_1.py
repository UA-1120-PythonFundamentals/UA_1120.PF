class polygon():
    def __init__(self, length, width):
        self.length = length
        self.width = width


class rectangle(polygon):
    def cra(self):
        area = length * width
        return area


length = int(input("Input length: "))
width = int(input("Input width: "))
print(f"Rectangle area is {rectangle(length, width).cra()}")
