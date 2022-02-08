import re

pattern = r"(?P<Day>\d{2})(?P<separ>[-/\.])(?P<Month>[A-Z][a-z]{2})(?P=separ)(?P<Year>\d{4})"
text = input()

valid_date = re.finditer(pattern, text)
for date in valid_date:
    curr_date = date.groupdict()
    print(f"Day: {curr_date['Day']}, Month: {curr_date['Month']}, Year: {curr_date['Year']}")
