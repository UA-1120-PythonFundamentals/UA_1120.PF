def calculate_character_counts(input_string):

  character_counts = {}

  for char in input_string:
      if char in character_counts:
          character_counts[char] += 1
      else:
          character_counts[char] = 1

  return character_counts

input_str = "hello"
result = calculate_character_counts(input_str)
print(result) 