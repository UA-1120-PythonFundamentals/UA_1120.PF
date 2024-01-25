def validation(user_name):
  has_lower_upper = any(char.islower() or char.isupper() for char in user_name)
  has_digit = any(char.isdigit() for char in user_name)
  has_special_char = any(char in ["$", "#", "@"] for char in user_name)
  valid_length = 6 <= len(user_name) <= 16

  return has_lower_upper and has_digit and has_special_char and valid_length

user_input = input("Enter your password: ")
result = validation(user_input)

print(result)