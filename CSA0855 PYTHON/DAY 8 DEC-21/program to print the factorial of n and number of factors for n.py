def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def count_factors(n):
    if n <= 0:
        return "Number must be positive."
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


n = int(input("Enter a positive integer: "))
fact = factorial(n)
factors_count = count_factors(n)

print(f"The factorial of {n} is: {fact}")
print(f"The number of factors of {n} is: {factors_count}")
