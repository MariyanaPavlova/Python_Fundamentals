text = input()

index = 0

while index < len(text)-1:
    if text[index] == text[index+1]:
        el_to_repl = f'{text[index]}{text[index+1]}'
        text = text.replace(el_to_repl, text[index])
        index = 0
    else:
        index +1

print(text)

===================
text = input()
same = None

for i in text:
    if i != same:
        print(i, end='')
        same = i