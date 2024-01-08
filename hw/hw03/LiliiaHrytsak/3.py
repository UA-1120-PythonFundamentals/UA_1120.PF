def swap_values1(num1, num2):
    num1, num2 = num2, num1
    return num1, num2


def swap_values2(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return num1, num2


print(swap_values1(1, 2))
print(swap_values2(1, 2))
