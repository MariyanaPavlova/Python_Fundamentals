data = input()

while True:
    command = input()
    if command == "Reveal":
        break
    command_sp = command.split(":|:")
    do = command_sp[0]

    if do == "InsertSpace":
        ind = int(command_sp[1])
        data = data[:ind] + " " + data[ind:]
        print(data)

    elif do == "Reverse":
        substring = command_sp[1]

        if substring in data:
            data = data.replace(substring, "", 1)
            reverse = substring[::-1]
            data = data + reverse
            print(data)
        else:
            print("error")

    elif do == "ChangeAll":
        substring = command_sp[1]
        replacemant = command_sp[2]

        data = data.replace(substring, replacemant)
        print(data)
print(f'You have a new text message: {data}')