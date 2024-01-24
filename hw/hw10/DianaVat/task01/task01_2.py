class human:
    def __init__(self,name):
       self.name = name
    def message(self):
       print(f"Hello, my {self.name}")
    def homosapiens(self):
       print("Hello, my Homosapiens")
    @staticmethod
    def staticMessage():
       print("You are beautiful")
a=human(input("Say me your name: "))
a.message()
a.homosapiens()  
a.staticMessage()  