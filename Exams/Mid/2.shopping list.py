initial_list = input().split('!')

commands = input()

while commands != 'Go Shopping!':
    curr_command = commands.split(' ')

    first = curr_command[0]
    second = curr_command[1]

    if first == 'Urgent':
        if second in initial_list:
            pass
        else:
            initial_list.insert(0, second)
    elif first == 'Unnecessary':
        if second in initial_list:
            initial_list.remove(second)
        else:
            pass
    elif first == 'Correct':
        third = curr_command[2]
        for i in range(len(initial_list)):
            if second in initial_list[i]:
                initial_list.remove(second)
                initial_list.insert(i, third)
        else:
            pass
    elif first == 'Rearrange':
        if second in initial_list:
            initial_list.remove(second)
            initial_list.append(second)
        else:
            pass

    commands = input()

print(', '.join(initial_list))