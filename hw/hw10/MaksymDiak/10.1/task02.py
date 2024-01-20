class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Hello, {self.name}!"

    @classmethod
    def species(c):
        return "Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "Arbitrary message."
