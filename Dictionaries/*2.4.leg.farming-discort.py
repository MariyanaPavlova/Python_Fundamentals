def print_remaining_shards(legendary_item, junk):
    sorted_resources = sorted(legendary_item.items(), key=lambda r: (-r[1], r[0]))
    sorted_junk = sorted(junk.items(), key=lambda j: j[0])

    for resource, qty in sorted_resources:
        print(f"{resource}: {qty}")

    for junk, qty in sorted_junk:
        print(f"{junk}: {qty}")


resources = input().split()

legendary_item = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

while True:
    for i in range(0, len(resources), 2):
        qty = int(resources[i])
        item = resources[i + 1].lower()

        if item in legendary_item:
            legendary_item[item] += qty
        else:
            if item not in junk:
                junk[item] = int(qty)
            else:
                junk[item] += int(qty)

        for _ in legendary_item.keys():
            if legendary_item["shards"] >= 250:
                legendary_item["shards"] -= 250
                print("Shadowmourne obtained!")
                print_remaining_shards(legendary_item, junk)
                exit()
            elif legendary_item["fragments"] >= 250:
                legendary_item["fragments"] -= 250
                print("Valanyr obtained!")
                print_remaining_shards(legendary_item, junk)
                exit()
            elif legendary_item["motes"] >= 250:
                legendary_item["motes"] -= 250
                print("Dragonwrath obtained!")
                print_remaining_shards(legendary_item, junk)
                exit()
    resources = input().split()