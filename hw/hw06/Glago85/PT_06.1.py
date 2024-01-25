#In the range from 1 to 10 determine:
# - even numbers that are divisible by 2,
# - odd numbers, which are divisible by 3,
# - numbers that are not divisible by 2 and 3.

even_div_2 = []
odd_div_3 = []
not_div_2_3 = []
for n in range(1, 11):
    if n % 2 == 0:
        even_div_2.append(n)
    elif n % 3 == 0:
        odd_div_3.append(n)
    else:
        not_div_2_3.append(n)
print("Even numbers that are divisible by 2: ", even_div_2)
print("Odd numbers, which are divisible by 3: ", odd_div_3)
print("Numbers that are not divisible by 2 and 3: ", not_div_2_3)