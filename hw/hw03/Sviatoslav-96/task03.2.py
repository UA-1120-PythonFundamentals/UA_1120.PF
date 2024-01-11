def product_of_digits(number):
    digits = [int(digit) for digit in str(number)]
    product = 1
    for digit in digits:
     product *= digit
    return product
number = 4282
result = product_of_digits(number)
print(f"{result}")




def reverse_number(number):
   reversed_number = int(str(number)[::-1])
   return reversed_number
number = 4282
reversed_result = reverse_number(number)
print(f"{reversed_result}")




def sort_digits_increasing_order(number):
    sorted_number = int("".join(sorted(str(number))))
    return sorted_number
number = 4282
sorted_result = sort_digits_increasing_order(number)
print(f"{sorted_result}")