array = [int(index) for index in input().split()]
command = input()

while not command == 'end':
    command_i = command.split(' ')
    do = command_i[0]

    if do == 'swap':
        ind1 = int(command_i[1])
        ind2 = int(command_i[2])
        array[ind1], array[ind2] = array[ind2], array[ind1]

    elif do == 'multiply':
        ind1 = int(command_i[1])
        ind2 = int(command_i[2])
        array[ind1] = array[ind1] * array[ind2]

    elif do == 'decrease':
        for i in range(len(array)):
            array[i] -=1

    command = input()
print(*array, sep=', ')