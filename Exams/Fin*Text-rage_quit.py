data = input()

text = ""
digit = ""
outt = ""

for i in range(len(data)):
    if not data[i].isdigit():
        text += data[i].upper()
        continue
    if i != (len(data)-1) and data[i+1].isdigit():
        digit += data[i]
        continue

    digit += data[i]
    outt += text * int(digit)
    text = ""
    digit = ""

unique = len(set(outt))
print(f'Unique symbols used: {unique}')
print(f'{outt}')
