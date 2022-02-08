data = input()

dict = {}

while data != 'Lumpawaroo':
    is_found = False

    if "|" in data:
        side, user = data.split(" | ")

        for i in dict:
            if user in dict[i]:
                is_found = True
                break
    else:
        user, side = data.split(" -> ")

        for i in dict:
            if user in dict[i]:
                dict[i].remove(user)

    if is_found:
        data = input()
        continue

    if side not in dict:
        dict[side] = []
    dict[side].append(user)

    if "->" in data:
        print(f"{user} joins the {side} side!")

    data = input()

sorted_sides = sorted(dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
for side, users in sorted_sides:
    if len(users) > 0:
        print(f'Side: {side}, Members: {len(users)}')

    for user in sorted(users):
        print(f'! {user}')



# sides = {
#     'dark_side': ['dark1', 'Gdark2', 'zdark'],
#     'light_side': ['light', 'light2', 'light3']
#         }
#
#
# sorted_sides = sorted(sides.items(), key=lambda kvp: -len(kvp[1]))
# for side, users in sorted_sides:
#     print(f'Side: {side}, Members{len(users)}!')
#     for user in sorted(users):
#         print(f'! {user}')