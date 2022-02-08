lenght = int(input())
command = input()

train=[0 for n in range(lenght)]
#train = [0] * lenght

while not command == 'End':
    listt = command.split()
    one = listt[0]
    two = int(listt[-1])
    position = int(listt[1])

    if one == 'add':
        train[-1] += two

    if one == 'insert':
        train[position] += two

    if one == 'leave':
       train[position] -= two

    command = input()
    print(train)