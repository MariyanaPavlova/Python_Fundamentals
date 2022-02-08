n = int(input())

dict = {}
new_dict = {}
last_dict = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in dict:
        dict[name] = 1
        new_dict[name] = grade
    else:
        dict[name] += 1
        new_dict[name] += grade

for name, grade in new_dict.items():
    aver = grade / dict[name]
    last_dict[name] = aver

sorted_dict = sorted(last_dict.items(), key=lambda x: -x[1])

for name, grade in sorted_dict:
    if grade >= 4.50:
        print(f'{name} -> {grade:.2f}')
