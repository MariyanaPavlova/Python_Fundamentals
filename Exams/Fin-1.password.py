text = input()

raw_pass = ""
command = input()

while command != "Done":
    command = command.split(" ")
    do = command[0]
    if do == "TakeOdd":
        for i in range(len(text)):
            if i % 2 !=0:
                raw_pass += text[i]
        print(raw_pass)
        text = raw_pass

    elif do == "Cut":
        ind_one = int(command[1])
        ind_two = int(command[2])
        end_ind = int(ind_one + ind_two)
        #text = text[:ind_one]+text[end_ind:]
        text = text.replace(text[ind_one:end_ind], "", 1)
        print(text)

    elif do == "Substitute":
        substring = command[1]
        replacement = command[2]

        if substring in text:
            text = text.replace(substring, replacement)
            print(text)
        else:
            print(f"Nothing to replace!")
    command = input()
print(f"Your password is: {text}")

