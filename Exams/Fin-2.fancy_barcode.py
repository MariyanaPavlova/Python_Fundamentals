import re

n = int(input())
pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"

for _ in range(n):
    barcode = input()
    matches = re.match(pattern, barcode)
    if matches:
        digits = re.findall(r"\d", barcode)
        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")