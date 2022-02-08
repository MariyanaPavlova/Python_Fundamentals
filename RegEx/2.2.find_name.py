import re

text = input()

pattern = r"(?<=\b _)[a-zA-Z]+($(?!=_)|(?=\s))"
outt = re.finditer(pattern, text)
outt = [num.group() for num in outt]
print(*outt, sep=",")