def pascals_triangle(n):
    triangle = []
    for i in range(n + 1):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def sum_of_nth_row(n):
    return 2 ** n

# Example usage
n = 4
triangle = pascals_triangle(n)
sum_nth_row = sum_of_nth_row(n)

print(f"Pascal's Triangle up to row {n}: {triangle}")
print(f"Sum of elements in row {n}: {sum_nth_row}")
