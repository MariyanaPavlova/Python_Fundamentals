def shoot(idx: int, power: int):
    if idx in range(len(targets_sequence)):
        targets_sequence[idx] -= power
        if targets_sequence[idx] <= 0:
            del targets_sequence[idx]
    return targets_sequence


def add(idx: int, value: int):
    if 0 <= idx <= len(targets_sequence):
        targets_sequence.insert(idx, value)
        return targets_sequence
    else:
        return print("Invalid placement!")


def strike(idx: int, radius: int):
    if idx - radius >= 0 and idx + radius <= len(targets_sequence) - 1:
        del targets_sequence[idx - radius:idx + radius + 1:]
        return targets_sequence
    else:
        return print("Strike missed!")


targets_sequence = [int(targets) for targets in input().split()]
command = input().split()
command_action = command[0]

while command_action != "End":
    command_num_one = int(command[1])
    command_num_two = int(command[2])

    if command_action == "Shoot":
        shoot(command_num_one, command_num_two)
    elif command_action == "Add":
        add(command_num_one, command_num_two)
    elif command_action == "Strike":
        strike(command_num_one, command_num_two)

    command = input().split()
    command_action = command[0]

print(f"{'|'.join(str(i) for i in targets_sequence)}")