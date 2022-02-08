list = [0]*10

while True:
    command = input()
    if command == 'End':
        break

    command_l = command.split('-')
    first = int(command_l[0])
    second = command_l[1]
    list.pop(first)
    list.insert(first, second)

final = [i for i in list if i!=0]
print(final)
