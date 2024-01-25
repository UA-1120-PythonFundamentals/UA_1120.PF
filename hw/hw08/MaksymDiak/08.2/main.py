import re


def validation(password):
    if len(password) > 16 or len(password) < 6:
        return False
    elif not re.search(r"[a-z]+", password):
        return False
    elif not re.search(r"[A-z]+", password):
        return False
    elif not re.search(r"[0-9]+", password):
        return False
    elif not re.search(r"[$#@]+", password):
        return False
    else:
        return True


password = input("Enter your password: ")

if validation(password):
    print("Password is valid!")
else:
    print("Password is not valid!")
