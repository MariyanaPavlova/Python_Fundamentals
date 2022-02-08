a = input().split(' ')
aa=set(a)
count_a=11
count_b=11

for i in aa:
    if 'A' in i:
        count_a -=1
        if count_a <7:
            break
    if 'B' in i:
        count_b -=1
        if count_b <7:
            break
print(f'Team A - {count_a};', end=' ')
print(f'Team B - {count_b}')
if count_a <7 or count_b <7:
    print('Game was terminated')