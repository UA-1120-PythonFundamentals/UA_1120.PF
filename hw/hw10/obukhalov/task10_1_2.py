#!/usr/bin/env python


class Human:

    def __init__(self, name):
        self.name = name

    def greetings(self):
        print(f"Hello {self.name}!")

    @classmethod
    def homo(cls):
        species = "Homosapiens"
        return species

    @staticmethod
    def msg():
        arbitrary = "Some message..."
        return arbitrary


if __name__ == "__main__":

    person = Human("Oleg")

    person.greetings()
    print(person.homo())
    print(person.msg())
