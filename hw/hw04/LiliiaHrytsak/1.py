def temperature_convert():
    t = input("Enter the temperature in Celsius: ")
    try:
        t_num = float(t)
    except ValueError:
        return "Invalid input"
    if t_num < -273.15:
        return "Error: Temperature below absolute zero (-273.15°C)"
    res = round((t_num * 9/5 + 32),2)
    return f"{t}°C equivalent to {res}°F"


print(temperature_convert())