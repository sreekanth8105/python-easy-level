def calculate_student_users(total_users, staff_users):
    
    non_teaching_staff_users = staff_users // 3
    
    
    student_users = total_users - (staff_users + non_teaching_staff_users)
    
    return student_users


total_users = 856
staff_users = 126


student_users = calculate_student_users(total_users, staff_users)
print(f"Number of Student Users: {student_users}")
