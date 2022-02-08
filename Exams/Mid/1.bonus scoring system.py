count_stud = int(input())
count_lect = int(input())
in_bonus = int(input())

max = 0
attendance= 0

for i in range(count_stud):
    attend = int(input())
    bonus = attend/count_lect*(5+in_bonus)
    if bonus > max:
        max = bonus
        attendance=attend

print(f"Max Bonus: {round(max)}.")
print(f'The student has attended {attendance} lectures.')
