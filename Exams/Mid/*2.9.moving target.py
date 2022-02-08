targets = [int(targets) for targets in input().split()]
command = input()

while command != 'End':
    command = command.split(' ')

    com = command[0]
    ind = int(command[1])
    value = int(command[-1])

    if com == 'Shoot':
        if ind in range(len(targets)):
            targets[ind] -= value
            if targets[ind] <=0:
                del targets[ind]

    if com == 'Add':
        if ind in range(len(targets)):
            targets.insert(ind, value)
        else:
            print("Invalid placement!")

    if com == 'Strike':
        if ind - value >=0 and ind + value <= len(targets)-1:
            del targets[ind-value:ind+value+1:]
        else:
            print('Strike missed!')

    command = input()

print(f"{'|'.join(str(i) for i in targets)}")