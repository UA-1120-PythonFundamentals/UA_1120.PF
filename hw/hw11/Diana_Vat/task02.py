def week(number):
    try:
        number = int(number)
        if number >0:
            number = number %7
            match number:
                case 1:
                    print("Monday")
                case 2:
                    print("Tuesday")
                case 3:
                    print("Wednesday")
                case 4:
                    print("Thursday")
                case 5:
                    print("Friday")
                case 6:
                    print("Saturday")
                case 0:
                    print("Sunday")
        else:
            raise ValueError
        
    except ValueError as err:
        print("Error....")
number_input = input("Enter number : ")
week(number_input)