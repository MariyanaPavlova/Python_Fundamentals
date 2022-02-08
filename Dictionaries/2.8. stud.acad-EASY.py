n = int(input())

grades = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

filtered_grades = {}

for student_name, grade in grades.items():
    avr_grade = sum(grade) / len(grade)
    if avr_grade >= 4.50:
        filtered_grades[student_name] = avr_grade

sorted_best_stud = sorted(filtered_grades.items(), key=lambda kvp: kvp[1], reverse=True)

for student_name, grade in sorted_best_stud:
    print(f'{student_name} -> {grade:.2f}')



