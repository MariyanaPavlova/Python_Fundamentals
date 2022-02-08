text = input()

outt = ""
for i in range(len(text)):
    if text[i] == ":":
        outt += text[i]
        outt += text[i+1]
        print(outt)
        outt = ""



