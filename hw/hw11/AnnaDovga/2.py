def week(day_number):
    if day_number > 7 or day_number < 1:
        raise ValueError("Incorrect number")
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(f"Day of the week: {days_of_week[day_number - 1]}")

day = int(input("Write day of week as number form 1 to 7:\n"))
try:
    week(day)
except ValueError as e:
    print(e)
