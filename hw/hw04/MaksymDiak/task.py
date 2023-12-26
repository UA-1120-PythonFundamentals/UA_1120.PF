
t = float(input("Enter the temperature in Celsius: "))

if t < -273.15:
    print(f'Error: Temperature below absolute zero (-273.15)')
else:
    print(f'{t}°C is equivalent to {(t * 9/5) + 32}°F')
