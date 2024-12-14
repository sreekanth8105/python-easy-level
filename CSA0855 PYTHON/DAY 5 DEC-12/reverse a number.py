def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10  # Get the last digit
        reversed_num = (reversed_num * 10) + digit  # Append it to the reversed number
        num //= 10  # Remove the last digit from the original number
    return reversed_num


number = 12345
print("Reversed Number:", reverse_number(number))
