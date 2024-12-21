def get_letter_for_number(number):
  """
  Returns the letters associated with a given number on a phone keypad.

  Args:
      number: The number on the keypad.

  Returns:
      A string of letters associated with the number, or an empty string if the number is invalid.
  """
  keypad = {
      2: "abc",
      3: "def",
      4: "ghi",
      5: "jkl",
      6: "mno",
      7: "pqrs",
      8: "tuv",
      9: "wxyz"
  }
  return keypad.get(number, "")
