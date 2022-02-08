text = input()

new_str = ""
strength = 0


for i in range(len(text)):
    if text[i] == ">":
        new_str += ">"
        strength += int(text[i+1])

    else:
        if strength > 0:
            strength -= 1
        else:
            new_str += text[i]

print(new_str)
