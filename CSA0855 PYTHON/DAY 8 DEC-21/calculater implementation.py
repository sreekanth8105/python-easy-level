def calculate(s: str) -> int:
    stack, current_number, operation = [], 0, '+'

    for i, char in enumerate(s + '+'):
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        if char in "+-*/" or i == len(s): 
            if operation == '+':
                stack.append(current_number)
            elif operation == '-':
                stack.append(-current_number)
            elif operation == '*':
                stack[-1] *= current_number
            elif operation == '/':
                stack[-1] = int(stack[-1] / current_number)  
            operation, current_number = char, 0
            return sum(stack)

#
print(calculate("3+2*2"))  # Output: 7
print(calculate(" 3/2 "))  # Output: 1
print(calculate(" 3+5 / 2 "))  # Output: 5
