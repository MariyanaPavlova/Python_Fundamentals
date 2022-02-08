dung_room = input().split('|')

health = 100
bitcoin = 0
tipe = 0
cell_value = 0
room_count = 0

for i in dung_room:
    curr_cell = i.split(' ')
    tipe = curr_cell[0]
    cell_value = int(curr_cell[-1])

    room_count += 1

    if tipe == 'potion':
        if health < 100:
            health += cell_value
            if health > 100:
                cell_value = abs(health-100-cell_value)
                health = 100
        print(f'You healed for {cell_value} hp.')
        print(f'Current health: {health} hp.')

    elif tipe == 'chest':
        bitcoin += cell_value
        print(f'You found {cell_value} bitcoins.')

    else:
        health -= cell_value
        if health > 0:
            print(f'You slayed {tipe}.')
        else:
            print(f'You died! Killed by {tipe}.')
            print(f'Best room: {room_count}')
            exit()

print(f"You've made it!")
print(f'Bitcoins: {bitcoin}')
print(f'Health: {health}')
