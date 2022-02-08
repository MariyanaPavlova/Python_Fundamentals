command = input()
dict = {}

while not command == 'stop':
    quantity = int(input())

    if command not in dict:
        dict[command] = quantity
    else:
        dict[command] += quantity

    command = input()

for key, quantity in dict.items():
    print(f'{key} -> {quantity}')

# или така:
[print(f"{key} -> {quantity}") for key, quantity in dict.items()]