def separate_vowels_consonants(input_string):
    vowels = "aeiouAEIOU"
    consonants = ""
    vowels_found = ""

    for char in input_string:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels:
                vowels_found += char + " "
            else:
                consonants += char + " "

    print("Vowels:", vowels_found.strip())
    print("Consonants:", consonants.strip())


input_string = "engineeringv"
separate_vowels_consonants(input_string)
