
def convert_binary():
    binary_input = input("Enter a binary number: ")
    
    decimal_value = int(binary_input, 2)
    
    octal_value = oct(decimal_value)
    
    print(f"Decimal: {decimal_value}")
    print(f"Octal: {octal_value[2:]}") 
convert_binary()
