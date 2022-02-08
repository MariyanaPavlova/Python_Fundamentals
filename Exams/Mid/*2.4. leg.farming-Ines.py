data = input()

items = {"shards": 0, 'fragments': 0, 'motes': 0}
junk_items = {}
key_materials = {"shards": 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
is_obtained = False

while not is_obtained:
    split_data = data.split()

    for i in range(0, len(split_data), 2):
        if is_obtained:
            break

        qty = int(split_data[i])
        material = split_data[i+1].lower()

        if material in items:
            items[material] += qty
        else:
            if material not in junk_items:
                junk_items[material] = qty
            else:
                junk_items[material] += qty

        for material, qty in items.items():
            if qty >= 250:
                is_obtained = True
                items[material] -= 250
                print(f'{key_materials[material]} obtained!')
                break
    if is_obtained:
        break
    data = input()

sorted_items = sorted(items.items(), key=lambda kvp: (-kvp[1], kvp[0]))

for material, qty in sorted_items:
    print(f'{material}: {qty}')

sorted_junks = sorted(junk_items.items(), key=lambda kvp: kvp[0])

for material, qty in sorted_junks:
    print(f'{material}: {qty}')
