def swap(array, first_index, second_index):
    array[first_index], array[second_index] = array[second_index], array[first_index]
    return array


def multiply(array, pending_action, first_index, second_index):
    multiplied_number = array[first_index] * array[second_index]
    array[first_index] = multiplied_number
    return array


def decrease_all_numbers(array, pending_action):
    for i in range(len(array)):
        array[i] -= 1
    return array


array_values = list(map(int, input().split(' ')))
data = input().split(' ')

while not data[0] == 'end':
    command = data[0]

    if command == 'swap':
        index_1 = int(data[1])
        index_2 = int(data[2])
        swap(array_values, index_1, index_2)
    elif command == 'multiply':
        index_1 = int(data[1])
        index_2 = int(data[2])
        multiply(array_values, command, index_1, index_2)
    elif command == 'decrease':
        decrease_all_numbers(array_values, command)

    data = input().split(' ')

print(*array_values, sep=', ')
