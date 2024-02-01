try:
  number = int(input("Enter a number: "))
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  if 0 <= number < 7:
      print(days[number])
  else:
      print("Invalid number")
except ValueError:
  print("Invalid input. Please enter a valid number.")