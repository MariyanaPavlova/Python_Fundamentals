num = int(input())
b=None

for i in range(1, num+1):
    num_string = str(i)
    result =0
    for i1 in num_string:
        result += int(i1)
    if result == 5 or result == 7 or result ==11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')