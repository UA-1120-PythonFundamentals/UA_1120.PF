import string

def password(p):
    if len(p) < 6 or len(p) > 16:
        return False
    
    a = set(string.ascii_letters)
    b = set(string.digits)
    c = set(string.punctuation)
    
    x = False
    y = False
    z = False

    for i in p:
        if i in a:
            x = True
        if i in b:
            y = True
        if i in c:
            z = True
        if x and y and z:
            return True
    return False

p = str(input('Enter your password: '))
print(password(p))   

if password(p):
    print('Your password is valid') 
else:
    print('Your password is not valid')



    
    
