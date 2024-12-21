
def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

def swap_with_tuple(a, b):
    a, b = b, a
    return a, b

if __name__ == "__main__":
    num1 = 5
    num2 = 10

    print("Original numbers: num1 =", num1, ", num2 =", num2)

    num1, num2 = swap_with_temp(num1, num2)
    print("After swapping with temp variable: num1 =", num1, ", num2 =", num2)

    num1, num2 = swap_without_temp(num1, num2)
    print("After swapping without temp variable: num1 =", num1, ", num2 =", num2)

    num1, num2 = swap_with_tuple(num1, num2)
    print("After swapping using tuple assignment: num1 =", num1, ", num2 =", num2)
