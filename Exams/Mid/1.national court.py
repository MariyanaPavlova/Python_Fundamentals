import math
one_empl_eff = int(input())
two_empl_eff = int(input())
tree_empl_eff = int(input())
people_count = int(input())

all_empl_eff = (one_empl_eff+two_empl_eff+tree_empl_eff)

total = math.ceil(people_count/all_empl_eff)
time = total
lunch = total // 3

if lunch != 0:
    time += lunch

print(f'Time needed: {math.ceil(time)}h.')
#
# employee_efficiency_1 = int(input())
# employee_efficiency_2 = int(input())
# employee_efficiency_3 = int(input())
# total_people = int(input())
# hours_needed = 0
# people_per_hour = employee_efficiency_1 + employee_efficiency_2 + employee_efficiency_3
#
# while total_people > 0:
#     hours_needed += 1
#     if hours_needed % 4 == 0:
#         hours_needed += 1
#     total_people -= people_per_hour
#
# print(f"Time needed: {hours_needed}h.")