#!/usr/bin/env python


def main():
    num = input("Enter the number that represents the day of the week: ")

    day_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }


    if num.isdigit():
        num = int(num)
    else:
        raise ValueError("You can only enter a number!")

    if num not in range(1,8):
        raise ValueError("You can only enter a number from 1 to 7!")


    print(f"The name of day is {day_of_week[num]}")
        

if __name__ == "__main__":
    main()
