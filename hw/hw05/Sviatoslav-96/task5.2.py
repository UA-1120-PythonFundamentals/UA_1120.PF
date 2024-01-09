def fibonacci(n):
  fib_sequence = [0, 1]

  while fib_sequence [-1] <= n:
      next_fib = fib_sequence[-1] + fib_sequence[-2]
      fib_sequence.append(next_fib)

  print(n, fib_sequence[:-1])

n = int(input("Please enter the number "))

fibonacci(n)