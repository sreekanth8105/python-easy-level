def count_factors(n):
  """
  This function counts the number of factors of a given number.

  Args:
    n: The number to count the factors of.

  Returns:
    The number of factors of n.
  """
  count = 0
  for i in range(1, n + 1):
    if n % i == 0:
      count += 1
  return count

n = int(input("Enter a number: "))

num_factors = count_factors(n)
print("The number of factors of", n, "is", num_factors)
