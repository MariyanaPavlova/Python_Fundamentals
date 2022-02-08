biscuits = input().split(', ')
command = input()

while not command == 'No More Money':
    com = command.split(' ')
    tipe = com[0]
    curr_bis = com[1]

    if tipe == 'OutOfStock':
        for i in range(len(biscuits)):
            if curr_bis == biscuits[i]:  #ако == се замени с in Chocolate влиза в WhiteChocolate
                biscuits[i] = 'None'

    elif tipe == 'Required':
        index = int(com[2])

        if 0 <= index < len(biscuits):
            if biscuits[index] != 'None':
                biscuits[index] = curr_bis

    elif tipe == 'Last':
        biscuits.append(curr_bis)

    command = input()

for i in biscuits:
    if i != 'None':
        print(i, end=' ')