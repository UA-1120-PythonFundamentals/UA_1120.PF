def age():
    try:
        age = int(input("Your age: "))
        if age < 0:
            raise ValueError("Age can't be negative!")
        elif age % 2 == 0:
            print("Age is even!")
        else:
            print("Age is odd!")
    except ValueError as e:
        print(e)


age()
