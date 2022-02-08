import re

t = input()

a = re.split(r'\:\s|\-', t)

print(a)
print(f'{a[1]}')
