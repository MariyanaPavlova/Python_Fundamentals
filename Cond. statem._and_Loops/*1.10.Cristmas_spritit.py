quantity = int(input())
days = int(input())

christmas_spirit=0
total_costs=0

for i in range(1, days+1):
    if i %11 == 0:
        quantity += 2

    if i %2 == 0:
        christmas_spirit += 5
        total_costs += 2 * quantity
    if i %3 == 0:
        christmas_spirit += 13
        total_costs += (5 +3) * quantity
    if i %5 == 0:
        christmas_spirit += 17
        total_costs += 15 * quantity
        if i %3 == 0:
            christmas_spirit += 30
    if i %10 == 0:
        christmas_spirit -= 20
        total_costs += (5+3+15)
    if i == days and i%10 == 0:
        christmas_spirit -= 30
print(f'Total cost: {total_costs}')
print(f'Total spirit: {christmas_spirit}')

