import re

text = input()

pattern = r'(::|\*\*)([A-Z][a-z]{2,})\1'
pattern_num = r"\d"

numbers = re.findall(pattern_num, text)
threshold = 1


for i in text:
    if i.isdigit():
         threshold *= int(i)

