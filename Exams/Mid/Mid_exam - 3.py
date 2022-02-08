numbers_list = input().split(', ')
point = int(input())
command = input()

numbers_int_list = [int(i) for i in numbers_list]

start = numbers_int_list[point]

left = 0
right = 0

for i in range(0, point):

    if command == 'cheap':
        if numbers_int_list[i] < start:
            left += numbers_int_list[i]
    elif command == 'expensive':
        if numbers_int_list[i] >= start:
            left += numbers_int_list[i]

for j in range(point+1, len(numbers_int_list)):

    if command == 'cheap':
        if numbers_int_list[j] < start:
            right += numbers_int_list[j]
    elif command == 'expensive':
        if numbers_int_list[j] >= start:
            right += numbers_int_list[j]

if left >= right:
    print(f'Left - {left}')
else:
    print(f'Right - {right}')
