empl = input().split(' ')
#empl = [int(i) for i in input().split(' ')]
factor = int(input())
num_happy=0

employee = list(map(lambda x: int(x)*factor, empl))

aver = sum(employee) /len(employee)
count = len(employee) /2

for i in employee:
    if i>aver:
        num_happy+=1
if num_happy>count:
    print(f'Score: {num_happy}/{len(employee)}. Employees are happy!')
else:
    print(f'Score: {num_happy}/{len(employee)}. Employees are not happy!')

