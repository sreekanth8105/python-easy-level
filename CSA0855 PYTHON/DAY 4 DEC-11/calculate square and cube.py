# Function to calculate square and cube
def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

# Main program
if __name__ == "__main__":
    try:
        # Input from user
        decimal_number = float(input("Enter a decimal number: "))
        square, cube = calculate_square_and_cube(decimal_number)
        
        # Display results
        print(f"The square of {decimal_number} is {square}.")
        print(f"The cube of {decimal_number} is {cube}.")
    except ValueError:
        print("Please enter a valid decimal number.")
