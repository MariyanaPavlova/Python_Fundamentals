import re
text = input()
food = []
cal = 0

pattern = r"(#|\|)(?P<f>([a-zA-Z]+|\s[a-zA-Z])+)\1(?P<y>[0-9]{2}\/[0-9]{2}\/[0-9]{2,4})\1(?P<c>[0-9]+)\1"

match = re.finditer(pattern, text)

for el in match:
    object = el.groupdict()
    food.append(object)
    cal += int(object["c"])

day_cal = cal //2000

print(f"You have food to last you for: {day_cal} days!")

for el in food:
    print(f"Item: {el['f']}, Best before: {el['y']}, Nutrition: {el['c']}")
print(food)

# re.finditer returns an iteratior object
# веднъж обходили ли го, не можем да го обхождаме–iterate пак

