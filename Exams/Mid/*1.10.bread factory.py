event = input().split('|')

energy = 100
coins = 100
cell_value = 0
bankrupt = False

for i in event:
    curr_event = i.split('-')
    tipe = curr_event[0]
    cell_value = int(curr_event[-1])

    if tipe == 'rest':
        if (energy+cell_value) > 100:
            energy = 100
            cell_value = 100-energy
        energy += cell_value
        print(f'You gained {cell_value} energy.')
        print(f'Current energy: {energy}.')

    elif tipe == 'order':
        if energy-30 >= 0:
            energy -= 30
            coins += cell_value
            print(f'You earned {cell_value} coins.')
        else:
            energy += 50
            print(f'You had to rest!')

    else:
        if coins-cell_value >0:
            coins -= cell_value
            print(f'You bought {tipe}.')
        else:
            print(f'Closed! Cannot afford {tipe}.')
            bankrupt = True
            break

if not bankrupt:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
