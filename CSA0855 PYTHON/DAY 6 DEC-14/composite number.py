def is_composite(n):
    return n > 3 and any(n % i == 0 for i in range(2, int(n**0.5) + 1))

def print_composite_numbers(a, b):
    return [num for num in range(a, b + 1) if is_composite(num)]
a, b = 10, 30
composite_numbers = print_composite_numbers(a, b)
print(composite_numbers)
