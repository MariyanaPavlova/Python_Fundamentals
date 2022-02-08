gifts = input().split()
command = input()

while command != 'No Money':
    curr_command = command.split()
    curr_gift = curr_command[1]

    if 'OutOfStock' in curr_command[0]:
        for i in range(len(gifts)):
            if curr_gift in gifts[i]:
                gifts[i] = 'None'
    elif 'Required' in curr_command[0]:
        i = int(curr_command[2])
        if 0 <= i < len(gifts):
            gifts[i] = curr_gift
    elif 'JustInCase' in curr_command:
        gifts[-1]=curr_gift
    command = input()

for i in gifts:
    if i != 'None':
        print(i, end=' ')
