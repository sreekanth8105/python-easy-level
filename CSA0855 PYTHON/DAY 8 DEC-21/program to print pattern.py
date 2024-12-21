
start_number = float(input("Enter the starting number: "))
num_lines = int(input("Max number of line printed: "))


for i in range(num_lines):
    for j in range(i + 1):
        print(f"{start_number + i + j:.1f}", end=" ")
    print()
