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
            zoo[name] = {"food": need_food, "area": area}
        else:
            zoo[name]["food"] += need_food

        if area not in area_zoo:
            area_zoo[area] = [name]
        else:
            if name not in area_zoo[area]:
                area_zoo[area].append(name)

    elif command == "Feed":
        food = int(add_s[1])
        z_area = zoo.get('area'[0])
        if name in zoo:
            if zoo[name]['food'] >=0:

                zoo[name]['food'] -= food
                if zoo[name]['food'] <=0:
                    print(f"{name} was successfully fed")
                    del zoo[name]



    data = input()
print(f'Animals:')
sorted_dict = (sorted(zoo.items(), key=lambda x: (-x[1]['food'], x)))

for key, value in sorted_dict:
    print(f"{key} -> {value['food']}g")
print('Areas with hungry animals:')

for key, value in sorted_dict.item():

    print(f" {value}: {value}")