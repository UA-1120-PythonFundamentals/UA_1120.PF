def count_digits(number):
    if not isinstance(number, (int)):
        return "Wrong data type"

    number = abs(int(number))

    num_digits = len(str(number))
    return num_digits

def gradeCalculator(grade):
    if grade < 0:
        print("Wrong number")
    elif grade >= 90 and grade <= 100:
        print("A")
    elif grade >= 80 and grade < 90:
        print("B")
    elif grade >= 70 and grade < 80:
        print("C")
    elif grade >= 60 and grade < 70:
        print("D")
    elif grade >= 0 and grade < 60:
        print("F")
    else:
        print("Invalid grade")

def sortNumbers(num1, num2, num3):
    if num1 <= num2 <= num3:
        print(num1, num2, num3)
    elif num1 <= num3 <= num2:
        print(num1, num3, num2)
    elif num2 <= num1 <= num3:
        print(num2, num1, num3)
    elif num2 <= num3 <= num1:
        print(num2, num3, num1)
    elif num3 <= num1 <= num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)

def calculator(number1, number2, operator):
    if operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "*":
        print(number1 * number2)
    elif operator == "/":
        if number2 == 0:
            print("Error: Division by zero")
        else:
            print(number1 / number2)
    else:
        print("Wrong operator")