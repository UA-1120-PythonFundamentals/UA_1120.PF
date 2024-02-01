class Human():
    def __init__(self,name):
        self_name = name
class Man(Human):
    def __init__(self,name):
        super().__init__(name)
class Woman(Human):
    def __init__(self,name):
        super().__init__(name)

def God():
    return [Man('Adam'),Woman("Eva")]

print(God())