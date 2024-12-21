import math

def count_factors(n):
    if n <= 0:
        return 0
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1  
            if i != n // i:  
                count += 1
    return count

n = 0
print(f"The number of factors of {n} is: {count_factors(n)}")
