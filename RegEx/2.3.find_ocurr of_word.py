import re

text = input()
word = input()

pattern = rf'\b{word}\b'
x = re.findall(pattern, text, re.IGNORECASE)
print(len(x))