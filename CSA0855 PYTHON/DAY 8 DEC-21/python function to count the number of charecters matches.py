def matches(string1, string2):
    # Initialize a counter for matches
    count = 0
    
    # Iterate through both strings using zip to pair characters
    for char1, char2 in zip(string1, string2):
        if char1 == char2:
            count += 1  # Increment count if characters match
            
    return count

# Example usage
result = matches("hello", "hallo")
print(result)  # Output: 4
