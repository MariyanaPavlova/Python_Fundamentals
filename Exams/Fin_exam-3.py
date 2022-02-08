data = input()

zoo = {}
area_zoo = {}
while not data == "EndDay":
    data = data.split(":")
    command = data[0]
    add = data[1]
    add_s = add.split("-")
    name = add_s[0]

    if command == "Add":
        need_food = int(add_s[1])
        area = add_s[2]

        if name not in zoo:
            zoo[name] = need_food
        else:
            zoo[name] += need_food

        if area not in area_zoo:
            area_zoo[area] = [name]
        else:
            if name not in area_zoo[area]:
                area_zoo[area].append(name)

    elif command == "Feed":
        name = add_s[0]
        food = int(add_s[1])
        if name in zoo:
            if zoo[name] >=0:
                zoo[name] -= food
                if zoo[name] <=0:
                    print(f"{name} was successfully fed")
                    del zoo[name]
                    for key, value in area_zoo.items():
                        if name in value:
                            value.remove(name)

    data = input()
print(f'Animals:')
sorted_dict = (sorted(zoo.items(), key=lambda x: (-x[1], x)))

for key, value in sorted_dict:
    print(f'{key} -> {value}g')
print('Areas with hungry animals:')

print(area_zoo)
sorted_area_zoo = (sorted(area_zoo.items(), key=lambda x:(-len(x[1]), x[0])))

for key, value in sorted_area_zoo:
    if len(value)!=0:
        print(f"{''.join(key)}: {len(value)}")
