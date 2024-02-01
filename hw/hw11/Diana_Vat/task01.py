def check_age(age):
    try:
        age = int(age)
        if age >=0:
            if not (age % 2):
                print(f"Your age is even = {age}")
            else:
                print(f"Your age is odd = {age}")
        else:
            raise Exception
    except Exception as err:
        print("Err")

input_age=input("Enter your age: ")
check_age(input_age)
