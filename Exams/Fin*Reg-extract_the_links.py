import re

text = input()

pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"
valids = []

while text:
    valid_sites = [el.group() for el in re.finditer(pattern, text)]
    text = input()
    if valid_sites:
        valids.extend(valid_sites)

print(*valids, sep="\n")