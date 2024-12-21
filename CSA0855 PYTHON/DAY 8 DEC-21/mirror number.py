def is_mirror_number(number):
  """
  This function checks if a number is a mirror number.

  Args:
      number: The number to check.

  Returns:
      True if the number is a mirror number, False otherwise.
  """

  number_str = str(number)
  reversed_number_str = number_str[::-1]
  return number_str == reversed_number_str

# Example usage
number = 12321
if is_mirror_number(number):
  print(f"{number} is a mirror number")
else:
  print(f"{number} is not a mirror number")
