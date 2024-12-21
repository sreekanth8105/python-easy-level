uppercase_count = 0
lowercase_count = 0
number_count = 0

while True:
    char = input("Enter a character (enter * to stop): ")
    if char == "*":
        break
    elif char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        number_count += 1

print(f"Number of uppercase characters: {uppercase_count}")
print(f"Number of lowercase characters: {lowercase_count}")
print(f"Number of numbers: {number_count}")
