"""def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        print(f"Error: Temperature below absolute zero ({-273.15}°C)")
    else:
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equivalent to {fahrenheit}°F")

try:
    celsius_input = float(input("Enter the temperature in Celsius: "))
    celsius_to_fahrenheit(celsius_input)
except ValueError:
    print("Error: Please enter a valid number for the temperature.")"""




def X_O(string):
    x_count = string.lower().count('x')
    o_count = string.lower().count('o')
    return x_count == o_count
result1 = X_O("xoxo")
print(result1)

result2 = X_O("xXoO")
print(result2)

result3 = X_O("abc")
print(result3)

result4 = X_O("xxxooo")