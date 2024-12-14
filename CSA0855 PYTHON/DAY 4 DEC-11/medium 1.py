def calculate_bread_cost():
    regular_price = 185.00
    discount_rate = 0.60

    # Input from user
    fresh_loaves = int(input("Enter the number of fresh loaves purchased: "))
    day_old_loaves = int(input("Enter the number of day old loaves purchased: "))

    # Validate input
    if fresh_loaves < 0 or day_old_loaves < 0:
        print("Please enter a non-negative number of loaves.")
        return

    # Calculating costs
    regular_cost = fresh_loaves * regular_price
    day_old_price = regular_price * (1 - discount_rate)
    day_old_cost = day_old_loaves * day_old_price
    total_cost = regular_cost + day_old_cost

    # Displaying results
    print(f"Regular price: Rs.{regular_price:.2f}")
    print(f"Amount of fresh loaves: Rs.{regular_cost:.2f}")
    print(f"Amount of day old loaves: Rs.{day_old_cost:.2f}")
    print(f"Total amount: Rs.{total_cost:.2f}")

# Call the function
calculate_bread_cost()
