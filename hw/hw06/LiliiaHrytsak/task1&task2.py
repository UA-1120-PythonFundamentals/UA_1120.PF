#Task1
l1=[]
l2=[]
l3=[]
for i in range(1,11):
    if i%2==0:
        l1.append(i)
    elif i%3==0:
        l2.append(i)
    else:
        l3.append(i)
print('even numbers:  ',*l1)
print('odd numbers that are diviseble by 3:  ', *l2)
print('numbers that are not diviseble by 2 and 3:  ',*l3)

#Task2

def check_login():
    while True:
        input_value = input("Write login: ")
        if input_value == 'First':
            print('Hello, user')
            break  # Exit the loop if the login is valid
        else:
            print('Error: not a valid login')

check_login()