def get_weekday():
    k = True
    while k:
        try:
            n = int(input("Enter a number in range 1-7 that corresponds to day of the week: "))
            if 1 <= n <= 7:
                if n == 1:
                    weekday = "Monday"
                elif n == 2:
                    weekday = "Tuesday"
                elif n == 3:
                    weekday = "Wednesday"
                elif n == 4:
                    weekday = "Thursday"
                elif n == 5:
                    weekday = "Friday"
                elif n == 6:
                    weekday = "Saturday"
                else:
                    weekday = "Sunday"
                print(f"The day corresponding to {n} is {weekday}.")
                k = False
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Please enter a valid numerical input.")


get_weekday()
