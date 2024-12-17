def reverse_words(s: str) -> str:
    # Step 1: Split the string into words
    words = s.split()
    
    # Step 2: Reverse the list of words
    reversed_words = words[::-1]  # or you can use words.reverse()
    
    # Step 3: Join the words with a single space
    result = ' '.join(reversed_words)
    
    return result

# Example usage
input_string = "  Hello   world  this is  a test  "
output_string = reverse_words(input_string)
print(f"Reversed Words: '{output_string}'")  # Output: 'test a is this world Hello'
