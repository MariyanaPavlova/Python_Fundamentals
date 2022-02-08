all_cells = input().split('#')
water = int(input())

total_effort =0
total_fire = 0
cells_values = []

for i in all_cells:
    curr_cell = i.split(' = ')
    tipe_of_fire = curr_cell[0]
    cell_value = int(curr_cell[-1])

    if tipe_of_fire == 'High':
        if not 81 <= cell_value <= 125:
            continue
    elif tipe_of_fire == 'Medium':
        if not 51 <= cell_value <= 80:
            continue
    elif tipe_of_fire == 'Low':
        if not 1 <= cell_value <= 50:
            continue
    if water < cell_value:
        continue

    cells_values.append(cell_value)
    water -= cell_value
    total_effort += cell_value * 0.25
    total_fire += cell_value

print('Cells:')
for j in cells_values:
    print(f' - {j}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')


