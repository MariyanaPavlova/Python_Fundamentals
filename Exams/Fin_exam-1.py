text = input()


command = input()
while not command == "End":
    command_s = command.split(" ")
    do = command_s[0]

    if do == 'Translate':
        char = command_s[1]
        repl = command_s[2]
        text = text.replace(char, repl)
        print(text)

    elif do == "Includes":
        str = command_s[1]
        x = str in text
        print(x)

        #if str in text:
            #print('True')
        #else:
            #print('False')
    elif do == "Start":
        str = command_s[1]
        y = text.startswith(str)
        print(y)

        #if text.startswith(str):
            #print('True')
        #else:
            #print('False')
    elif do == "Lowercase":
        text = text.lower()
        print(text)

    elif do == "FindIndex":
        char = command_s[1]
        char_found = text.rfind(char)
        print(char_found)

    elif do == "Remove":
        start_i = int(command_s[1])
        count = int(command_s[2])
        end_i = start_i+count
        if 0 <= start_i < len(text) and 0 <= end_i < len(text):

            text = text[:start_i] + text[end_i:]

        print(text)

    command = input()

