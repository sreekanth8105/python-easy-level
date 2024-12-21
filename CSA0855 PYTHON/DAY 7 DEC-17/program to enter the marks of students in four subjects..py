subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))
subject4 = int(input("Enter marks for subject 4: "))

total_marks = subject1 + subject2 + subject3 + subject4

aggregate = (total_marks / 400) * 100

if aggregate >= 75:
    grade = "Distinction"
elif aggregate >= 60:
    grade = "First Division"
elif aggregate >= 50:
    grade = "Second Division"
elif aggregate >= 40:
    grade = "Third Division"
else:
    grade = "Fail"

print("Total Marks:", total_marks)
print("Aggregate Percentage:", aggregate)
print("Grade:", grade)
