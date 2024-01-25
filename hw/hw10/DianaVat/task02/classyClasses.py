class Person:
    def init(self,name,age):
        self.info= f"{name}s age is {age}"
        self.name = name
        self.age = age
    def get_info(self):
        return self.info