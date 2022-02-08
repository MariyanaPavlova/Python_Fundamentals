# import re
#
# pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
# text = input()
#
# valid_names = re.findall(pattern, text)
# print(*valid_names)
# #print(" ".join(valid_names))
#


import re


pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
names = input().split(", ")

valid_names = []

for name in names:
    match = re.match(pattern, name)
    if match:
        valid_names.append(match.group())
        
print(" ".join(valid_names))
