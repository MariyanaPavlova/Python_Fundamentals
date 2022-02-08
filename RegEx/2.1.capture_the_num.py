import re

text = input()
pattern = r"\d+"
all_num = []

while text:
    num = re.findall(pattern, text)
    all_num.extend(num)

    text = input()

print(*all_num)