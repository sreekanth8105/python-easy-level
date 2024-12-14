
def print_pattern(rows):
    for i in range(1, rows + 1):
        
        row_values = [f"{j/10:.1f}" for j in range(1, i + 1)]
        
        print(" ".join(row_values))


if __name__ == "__main__":
    try:
        num_rows = int(input("Enter the number of rows: "))
        print_pattern(num_rows)
    except ValueError:
        print("Please enter a valid integer.")
