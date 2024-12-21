def find_nth_odd_number(n):
  """
  This function finds the nth odd number after n odd numbers.

  Args:
    n: The number of odd numbers to skip.

  Returns:
    The nth odd number after n odd numbers.
  """

  # Calculate the total number of odd numbers to consider
  total_odd_numbers = 2 * n + 1

  # Return the nth odd number after n odd numbers
  return total_odd_numbers

# Example usage
n = 5
nth_odd_number = find_nth_odd_number(n)
print(f"The {n}th odd number after {n} odd numbers is {nth_odd_number}")
