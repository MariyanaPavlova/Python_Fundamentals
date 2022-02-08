one = input()
two = input()

for i in range(len(one)):
    if one[i] != two[i]:
        for two_i in range(0, i+1):
            print(two[two_i], end='')
        for one_i in range(i+1, len(one)):
            print(one[one_i], end='')
        print()