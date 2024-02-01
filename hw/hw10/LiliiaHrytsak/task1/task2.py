class Human():
    def __init__(self, *all_names):
        self.all_names = all_names

    def to_welcome(self):
        for _ in self.all_names:
            print(f'Welcome dear {_}')

    @classmethod
    def define_spices(cls):
        print(f"There are spices of {cls.__name__}")

    @staticmethod
    def arbitrary_massage():
        print('You are unique in this world')


an = Human('a','b','s','d')
an.to_welcome()
an.define_spices()
an.arbitrary_massage()

