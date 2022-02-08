username = input().split(", ")

valid_symbols = ["_", "-"]

for i in username:
    if 3 <=len(i)<= 16 and i.isalnum():
        print(i)
    for j in i:
        if j in valid_symbols:
            print(i)
