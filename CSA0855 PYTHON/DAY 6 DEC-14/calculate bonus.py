def calculate_bonus(salary, grade):
    bonus = salary * (0.05 if grade == 'A' else 0.10 if grade == 'B' else 0)
    if salary < 10000:
        bonus += salary * 0.02
    return bonus, salary + bonus
salary = float(input("Enter salary: "))
grade = input("Enter grade (A/B): ").upper()
bonus, total_salary = calculate_bonus(salary, grade)
print(f"Bonus: ${bonus:.2f}, Total Salary: ${total_salary:.2f}")
