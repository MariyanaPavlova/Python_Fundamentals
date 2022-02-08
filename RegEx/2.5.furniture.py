import re

pattern = r">>(?P<name>[A-Z a-z]+)<<(?P<price>\d+(|\.)\d+)\!(?P<quantity>\d+)"
line = input()
furn_names = []
total_spend = 0

while not line == "Purchase":
    match = re.match(pattern, line)
    if match:
        data = match.groupdict()
        furn_names.append(data['name'])
        total_spend += int(data['quantity']) * float(data['price'])
    line = input()

print("Bought furniture:")
if furn_names:
    print("\n".join(furn_names))
print(f"Total money spend: {total_spend:.2f}")