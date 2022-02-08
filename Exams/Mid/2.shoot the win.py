targets = [int(el) for el in input().split(' ')]
shot = []
command_ = input()

while not command_ == 'End':
    command = int(command_)

    if command < len(targets) and command not in shot:
        shot.append(command)

        for i in range(len(targets)):
            if i not in shot:
                if targets[i] <= targets[command]:
                    targets[i] = targets[i] + targets[command]
                else:
                    targets[i] = targets[i] - targets[command]

        targets[command] = -1
    command_ = input()

print(f"Shot targets: {targets.count(-1)} -> {' '.join([str(el) for el in targets])}")
