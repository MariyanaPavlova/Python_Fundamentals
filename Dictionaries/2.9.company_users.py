command = input()

users = {}

while not command == 'End':
    command_s = command.split(' -> ')
    comp_name = command_s[0]
    empl_id = command_s[1]

    if comp_name not in users:
        users[comp_name] = [empl_id]
    else:
        if empl_id not in users[comp_name]:
            users[comp_name].append(empl_id)

    command = input()

sorted_users = sorted(users.items(), key=lambda x: x[0])

for key, value in sorted_users:
    print(f'{key}')
    for i in value:
        print(f'-- {i}')



