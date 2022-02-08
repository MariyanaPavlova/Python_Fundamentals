act_key = input()
data = input()

while not data == "Generate":
    data = data.split(">>>")

    if data[0] == "Contains":
        substring = data[1]
        if substring in act_key:
            print(f"{act_key} contains {substring}")
        else:
            print("Substring not found!")

    elif data[0] == "Flip":
        case = data[1]
        start_ind = int(data[2])
        end_ind = int(data[3])
        if case == "Upper":
            # for i in range(start_ind, end_ind):  --- дава 80/100
            #     if act_key[i].islower():
            #          act_key = act_key.replace(act_key[i], (act_key[i].upper()))

            act_key = act_key.replace(act_key[start_ind:end_ind], act_key[start_ind:end_ind].upper())
            print(act_key)

        if case == "Lower":
            act_key = act_key.replace(act_key[start_ind:end_ind], act_key[start_ind:end_ind].lower())
            print(act_key)

    elif data[0] == "Slice":
        start_ind = int(data[1])
        end_ind = int(data[2])
        act_key = act_key.replace(act_key[start_ind:end_ind], "")
        print(act_key)

    data = input()

print(f"Your activation key is: {act_key}")