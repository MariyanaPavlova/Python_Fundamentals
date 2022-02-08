n = int(input())

dict = {}

for i in range(n):
    command = input().split(" ")
    username = command[1]

    if command[0] == 'register':
        plate = command[2]
        if username not in dict:
            dict[username] = plate
            print(f'{username} registered {plate} successfully')
        else:
            print(f'ERROR: already registered with plate number {plate}')

    elif command[0] == "unregister":
        if username not in dict:
            print(f"ERROR: user {username} not found")
        else:
            del dict[username]
            print(f"{username} unregistered successfully")

[print(f'{key} => {value}') for key, value in dict.items()]