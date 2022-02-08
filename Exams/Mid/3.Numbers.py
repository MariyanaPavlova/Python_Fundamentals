lists = [int(i) for i in input().split()]

new = []
sum = 0
count = 0

for i in range(len(lists)):
    sum += lists[i]
    count += 1

aver = sum/count

for i in range(len(lists)):
    if int(lists[i]) >= aver:
        new.append(lists[i])

new_s = new.sort(reverse = True)

if aver !=0 and aver!=1:
    print(*new[:5], sep=' ')
else:
    print('No')
