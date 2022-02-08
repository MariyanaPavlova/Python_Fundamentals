targets = [int(el) for el in input().split()]
shot_targets = []
command = input()

while not command == "End":
    index = int(command)
    if index not in shot_targets and 0 <= index < len(targets):
        shot_targets.append(index)
        for i in range(len(targets)):
            if i not in shot_targets:
                if targets[i] <= targets[index]:
                    targets[i] = targets[i] + targets[index]
                else:
                    targets[i] = targets[i] - targets[index]
        targets[index] = -1
    command = input()

print(f"Shot targets: {targets.count(-1)} -> {' '.join([str(el) for el in targets])}")