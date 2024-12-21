def add_binary(a: str, b: str) -> str:
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0 or carry:
        carry += (int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0)
        result.append(str(carry % 2))
        carry //= 2
        i -= 1
        j -= 1

    return ''.join(reversed(result))

a = "1010"
b = "1011"
print(add_binary(a, b))  
