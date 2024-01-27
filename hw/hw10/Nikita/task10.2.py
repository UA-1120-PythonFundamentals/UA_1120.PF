class Human:
    def __init__(self, name):
        self.name = name
    def greet (self):
        print(f'Hi, {self.name}')
    def homosapiens(self):
        return('This is Homosapiens')
    @staticmethod
    def statickMessage():
        print('Hello, Human')
a = Human(input('Enter your name: '))

a.greet()
print(a.homosapiens())
a.statickMessage()

print()

