import re

def check(passw):
    if 6 > len(passw) or 16 < len(passw):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

password = input('Enter password ')
# password = 'asW3cn467fghhty$'

if check(password):
    print('Password OK')
else:
    print('Password invalid')