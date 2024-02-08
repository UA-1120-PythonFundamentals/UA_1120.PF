class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, {self.name}!")

    def species(self):
        print(f"{self.name} is Homosapiens.")

    @staticmethod
    def staticmethod():
        return "Homosapiens is ..."


person = Human("Ket")
person.hello()
person.species()
print(Human.staticmethod())
