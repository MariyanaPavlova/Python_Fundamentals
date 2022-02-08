year = int(input())

while True:
    year += 1
    year_s = str(year)
    if len(year_s) == len(set(year_s)):
        print(year)
        break