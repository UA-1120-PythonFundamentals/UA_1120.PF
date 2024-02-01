def process_age(age):
  try:
      if age < 0:
          raise ValueError("Age cannot be negative")
      if age % 2 == 0:
          print("Your age is even")
      else:
          print("Your age is odd")
  except ValueError as ve:
      print(ve)

try:
  age = int(input("Please enter your age: "))
  process_age(age)
except ValueError:
  print("Invalid input. Please enter a valid age.")