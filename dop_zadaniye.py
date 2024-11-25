grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(students)
average_grades = {'Johnny': [5, 3, 3, 5, 4], 'Bilbo': [2, 2, 2, 3], 'Steve': [4, 5, 5, 2], 'Khendrik': [4, 4, 3],
                  'Aaron': [5, 5, 5, 4, 5]}
for student_name, grade_average in zip(students_sort, grades):
    average_grade = sum(grade_average) / len(grade_average)
    average_grades[student_name] = average_grade
    print(average_grade)