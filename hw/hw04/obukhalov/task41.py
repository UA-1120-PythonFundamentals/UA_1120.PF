#!/usr/bin/env pyton


def main():
    while True:
        try:
            t = float(input(f"Enter the temperature in Celsius: "))
        except ValueError:
            print("Input error. Numbers only are accepted.\nTry again.")
            continue
        if t < -273.15:
            print(
                "Input error. The entered temperature is below absolute zero.\nTry again."
            )
            continue
        break

    f = (t * 9 / 5) + 32

    print(f"Temperature in Fahrenheit is: {f}")


if __name__ == "__main__":
    main()
