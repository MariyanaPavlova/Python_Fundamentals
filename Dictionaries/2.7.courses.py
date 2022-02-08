command = input()

dict ={}

while not command == 'end':
    commandd = command.split(" : ")
    course_name = commandd[0]
    student_name = commandd[1]

    if course_name not in dict:
        dict[course_name] = [student_name]
    else:
        dict[course_name].append(student_name)

    command = input()

sorted_dict = sorted(dict.items(), key=lambda x: (len(x[1])), reverse=True)

for course_name, student_name in sorted_dict:
    print(f'{course_name}: {len(student_name)}')

    student_sorted = sorted(student_name, reverse=False)
    for el in student_sorted:
        print(f'-- {el}')
