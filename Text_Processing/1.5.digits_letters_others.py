word = input()

digits = ""
letters = ""
others = ""

for i in word:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        others += i

print(digits)
print(letters)
print(others)