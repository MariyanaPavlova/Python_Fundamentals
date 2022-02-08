ode = input()

command = input()

while not command == "Decode":
    command_s = command.split("|")
    do = command_s[0]

    if do.startswith("Change"):
        old = command_s[1]
        new = command_s[2]
        code = code.replace(old, new)

    if do.startswith("Move"):
        num = int(command_s[1])
        move1 = code[:num]
        move_mid = code[num:]
        code = move_mid + move1

    elif do.startswith("Insert"):
        ind = int(command_s[1])
        value = command_s[2]
        if 0 <= ind <= len(code):
            beg = code[:ind]
            end = code[ind:]
            code = beg+value+end

    command = input()

print(f'The decrypted message is: {code}')