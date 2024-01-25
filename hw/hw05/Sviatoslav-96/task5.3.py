def calculate_factorial(n):
  if n < 0:
      return
  elif n == 0 or n == 1:
      return 1
  else:
      result = 1
      for i in range(2, n + 1):
          result *= i
      return result

n = int(input("Enter a number to calculate the factorial: "))

factorial_result = calculate_factorial(n)
print(factorial_result)