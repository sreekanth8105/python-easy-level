def is_perfect(num):
    return sum(i for i in range(1, num) if num % i == 0) == num

def perfect_numbers(n):
    count, num = 0, 1
    perfects = []
    while count < n:
        if is_perfect(num):
            perfects.append(num)
            count += 1
        num += 1
    return perfects

def factors(num, m):
    return [i for i in range(1, num + 1) if num % i == 0][:m]

def main(n, m):
    perfects = perfect_numbers(n)
    for p in perfects:
        print(f"Perfect Number: {p}, First {m} Factors: {factors(p, m)}")

# Example usage
n = 3  # Number of perfect numbers
m = 3  # Number of factors to display
main(n, m)
