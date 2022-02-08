import re
text = input()
pattern = r'(\/|\=)(?P<dest>[A-Z]{1}[A-Za-z]{2,})\1'

valid = re.finditer(pattern,text)
lenght =0
dest = []

for el in valid:
    object = el.groupdict()
    lenght += len(object["dest"])
    dest.append(object)
de=[]

for el in dest:
    de.append(el["dest"])

print(f'Destinations: {", ".join(de)}')
print(f"Travel Points: {lenght}")

=======================
import re

text = input()
pattern = r"(?<=(/|\=))([A-Z]{1}[a-zA-Z]{2,})(?=\1)"

valid_dest = [d.group() for d in re.finditer(pattern, text)]
travel_points = sum([len(d) for d in valid_dest])
#destin = []

#for d in re.finditer(pattern, line):
    #destin.append(d.group('dest'))
    #travel_points += len(d.group('destin'))

print(f'Destinations: {", ".join(valid_dest)}')
print(f'Travel Points: {travel_points}')