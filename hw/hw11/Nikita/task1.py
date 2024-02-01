def human_age():
    try:
        age = int(input('Enter your age: '))
        if age < 0:
            raise ValueError('Negative age! It can`t be')
        if age % 2 == 0:
            print('Your age is EVEN')
        else:
            print('Your age is ODD')
    except ValueError as error:
        print(error)    

human_age()