import math

def count_sorted_vowel_strings(n):
    # Calculate the number of sorted strings of length n
    return math.comb(n + 4, 4)

# Example usage:
n = -5
print(count_sorted_vowel_strings(n))  
