def temperatureConvert(c):
    if c > -273.15:
        print(f"{c}°C is equialent to {(c * (9/5) + 32)}°F")
    else:
        print("error")


x = float(input("enter the temperature: "))
temperatureConvert(x)