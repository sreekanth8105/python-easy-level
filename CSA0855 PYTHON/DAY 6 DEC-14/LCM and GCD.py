import math
from functools import reduce

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
gcd_result = reduce(gcd, numbers)
lcm_result = reduce(lcm, numbers)
print(f"GCD: {gcd_result}, LCM: {lcm_result}")
