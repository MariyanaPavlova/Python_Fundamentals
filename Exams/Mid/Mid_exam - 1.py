import math
budget = float(input())
students = int(input())
flour = float(input())
egg = float(input())
apron = float(input())

free_pack = 0
for el in range(1, students+1):
    if el % 5 == 0:
        free_pack += 1
students_20 = math.ceil(students*0.20)

price_apron = apron * (students + students_20)
price_egg = egg * 10 * students
price_flour = flour * (students - free_pack)

total_price = price_apron + price_egg + price_flour
diff = abs(budget - total_price)

if total_price <= budget:
    print(f'Items purchased for {total_price:.2f}$.')
else:
    print(f'{diff:.2f}$ more needed.')
