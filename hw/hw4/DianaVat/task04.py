temperature = input("Enter your temperature today in C, but only Integer/Float type: ")
temperature = float(temperature)

if temperature > -273.15:
    Fahrenheit = (temperature*9/5)+32
    print(f"Your temperature in Fahrenheit is:{Fahrenheit}")
        
else:
    print("Error:you Enter number > -273.15")