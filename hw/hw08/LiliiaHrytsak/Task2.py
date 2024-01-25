import re


def validate_password(password):
    # Define patern
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$')

    # Use re.match() to check if the password matches the pattern
    if pattern.match(password):
        return True
    else:
        return False


print(validate_password("a"))
print(validate_password("sA96778@"))