import re

n = int(input())

count =0

for i in range(n):
    text = input()

    username = r'(U\$)([A-Z][a-z]{3,})\1(P\@\$)([a-zA-Z]{5,}\d{1,})\3'
    # user = r"(?P<s1>(U\$))(?P<u>([A-Z][a-z]{2,}))(?P=s1)(?P<s2>(P\@\$))(?P<p>([a-zA-Z]{5,}\d{1,}))(?P=s2)"
    #
    # valid = [el.groupdict() for el in re.finditer(user, text)]
    # print([f'{i["u"]} {i["p"]}' for i in valid])
    #
    # a=5

    valid = re.findall(username, text)

    print(valid)
    if valid:
        count +=1
        print("Registration was successful")
        print(f'Username: {valid[0][1]}, Password: {valid[0][3]}')
    else:
        print(f'Invalid username or password')

print(f'Successful registrations: {count}')
