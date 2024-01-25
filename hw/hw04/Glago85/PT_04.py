#Temperature converter from Celsius to Fahrenheit
while True:
    try:
        temp = float(input('Enter the temperature in Celsius: '))
        break
    except ValueError:
        print('Error: You enter not valid number for the temperature. Try again')

if temp < -273.15:
    print('Error: Temperature below absolute zero (-273.15°C)')
else:
    print(f'{temp}°C is equivalent to {(temp * 9/5) + 32}°F')