def calculate_shipping_cost(num_items):
  """
  Calculates the shipping cost for an order based on the number of items.

  Args:
    num_items: The number of items in the order.

  Returns:
    The total shipping cost for the order.
  """
  if num_items <= 0:
    return 0.00
  elif num_items == 1:
    return 750.00
  else:
    return 750.00 + (num_items - 1) * 200.00

# Get the number of items from the user
num_items = int(input("Enter the number of items purchased: "))

# Calculate the shipping cost
shipping_cost = calculate_shipping_cost(num_items)

# Display the shipping cost
print(f"The shipping charge for your order is: ${shipping_cost:.2f}")
