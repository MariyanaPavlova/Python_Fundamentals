text = input()
comand = input()
new_text = ""

while not comand == "Play":

    comand_s = comand.split(" ")
    do = comand_s[0]

    if do == 'Move':
        i = int(comand_s[1])
        let = text[i]
        if 0 < i <= len(text):
            text = text.replace(let, "", 1)
            text = text+let

    elif do.startswith('Insert'):
            ind = int(comand_s[-1])
            one = text[:ind]
            next = text[ind:]
            text = one + " " + next

    elif do == "Reverse":
        subst = comand_s[1]
        if subst in text:
            text = text.replace(subst, "", 1)
            reverse = subst[::-1]
            text = text + reverse

    elif do.startswith('Exchange') and comand_s[1] == 'Tiles':
        new_let = "".join(comand_s[2:])
        count = int(len(new_let))
        my = text[count:]
        text = new_let+ my
        a = " ".join(text)
        print(a)
        exit()
    elif comand == "Pass":
        b = " ".join(text)
        print(b)
        exit()

    comand = input()

if " " in text:
    find = text.find(" ")
    text = text[:find]

print(f'You are playing with the word {text}.')
