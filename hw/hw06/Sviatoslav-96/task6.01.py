def classify_numbers(number):
  return number % 2 == 0 or number % 3 == 0
for number in range(1, 11):
   result = classify_numbers(number)
   
   print(f"{number} multiple of 2 and 3: {result}")