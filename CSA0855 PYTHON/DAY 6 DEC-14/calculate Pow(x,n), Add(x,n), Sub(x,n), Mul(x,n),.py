x = float(input("Enter x: "))
n = float(input("Enter n: "))
op = input("Choose operation (pow, add, sub, mul, div): ")
result = {
    'pow': x ** n,
    'add': x + n,
    'sub': x - n,
    'mul': x * n,
    'div': x / n if n != 0 else "Cannot divide by zero"
}.get(op, "Invalid operation")

print(f"Result: {result}")
