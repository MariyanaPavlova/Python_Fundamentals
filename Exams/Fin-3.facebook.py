status = {}
commands = input()
new_dict = {}
dict1 = {}
dict2 = {}
while commands != "Log out":
    data = commands.split(": ")
    if data[0] == "New follower":
        username = data[1]
        if username not in status:
            status[username] = {"likes": 0, "comments": 0}

    elif data[0] == "Like":
        username = data[1]
        likes = int(data[2])
        if username in status:
            status[username]["likes"] += likes

        else:
            status[username] = {"likes": likes, "comments": 0}

    elif data[0] == "Comment":
        username = data[1]

        if username in status:
            status[username]["comments"] += 1
        else:
            status[username] = {"likes": 0, "comments": 1}

    elif data[0] == "Blocked":
        username = data[1]
        if username not in status:
            print(f"{username} doesn't exist.")
        else:
            del status[username]

    commands = input()
print(f"{len(status)} followers")

for k, v in status.items():
    values = sum(v.values())
    new_dict[k] = values

dict_sort = sorted(new_dict.items(), key=lambda tkvp: (-tkvp[1], tkvp[0]))
for name, value in dict_sort:
    print(f"All sold {value}")