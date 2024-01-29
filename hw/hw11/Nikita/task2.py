def day_of_week():
    try:
        day = int(input('Enter a number of week: '))
        if day < 1 or day > 7:
            raise ValueError('Error! It can`t be. Only between 1 - 7')
        days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday',}
        print(f'The day of the week is: {days[day]}')
    except ValueError as error:
        print(error)

day_of_week()

