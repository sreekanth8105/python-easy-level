def factorial(n):
  """
  This function calculates the factorial of a given number.

  Args:
    n: The number to calculate the factorial of.

  Returns:
    The factorial of n.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)


n = int(input("Enter a number: "))

fact = factorial(n)

print("The factorial of", n, "is", fact)
