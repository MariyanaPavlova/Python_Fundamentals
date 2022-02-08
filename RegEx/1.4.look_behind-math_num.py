import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()

valid_num = re.finditer(pattern, text)
valid_num = [num.group() for num in valid_num]
print(*valid_num)