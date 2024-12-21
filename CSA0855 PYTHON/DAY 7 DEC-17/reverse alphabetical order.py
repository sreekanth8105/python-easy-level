def reverse_alphabetical_order(word):
  """
  Arranges the letters of a word alphabetically in reverse order.

  Args:
    word: The word to be sorted.

  Returns:
    The word with letters in reverse alphabetical order.
  """
  return ''.join(sorted(word, reverse=True))

# Example usage
word = "hello"
sorted_word = reverse_alphabetical_order(word)
print(f"The word '{word}' in reverse alphabetical order is '{sorted_word}'")
