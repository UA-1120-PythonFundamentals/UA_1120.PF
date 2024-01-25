def count_sheeps(sheep):
  count = 0
  for i in sheep:
      if i == True:
          count += 1

  return count

sheep_array = [True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, False, False, True, True]
result = count_sheeps(sheep_array)

pass