n = int(input())
checked = 0
free = 0

for i in range(1, n+1):
    chairs = input().split(' ')
    x = chairs[0]
    visitor = int(chairs[1])

    count = int(x.count('X'))
    checked = count-visitor
    free += (count-visitor)

    if checked < 0:
        print(f'{abs(checked)} more chairs needed in room {i}')

if free >=0:
    print(f'Game On, {free} free chairs left')
