def f():
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    try:
        day = int(input("Enter a day (number): "))
        if day < 1 or day > 7:
            raise ValueError("Error!")
        print(f"The {day}th day of the week is {days[day]}.")
    except ValueError as e:
        print(e)


f()
