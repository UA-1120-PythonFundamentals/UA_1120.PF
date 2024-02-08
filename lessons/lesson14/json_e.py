import json


class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"User(name={self.name}, age={self.age}, email={self.email})"

    def __repr__(self):
        return f"User(name={self.name}, age={self.age}, email={self.email})"


    def to_dict(self):
        return {"Name": self.name, "Age": self.age, "Email": self.email}

x = '{ "name":"Liubov", "age":25, "city":"Lviv"}' 

# t = json.loads(x)
# print(t)
# print(type(t))


# with open("lessons/lesson14/data/users.json") as file:
#     t = json.load(file)
#     print(t)

with open("lessons/lesson14/data/users.json") as file:
    data = json.load(file)
    users = []
    for user in data:
        users.append(User(**user))

print(users)
users_35p = [user for user in users if user.age >= 35]

with open("lessons/lesson14/data/users_35.json", "w") as file:
    data = [user.to_dict() for user in users]
    print(json.dumps(data))
    json.dump(data, file)
