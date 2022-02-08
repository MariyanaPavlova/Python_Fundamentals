n = int(input())

even = []
odds = []
pos = []
neg = []

for i in range(n):
    curr_num = int(input())

    if curr_num % 2 == 0:
        even.append(curr_num)
    if curr_num % 2 == 1:
        odds.append(curr_num)
    if curr_num < 0:
        neg.append(curr_num)
    if curr_num >= 0:
        pos.append(curr_num)

command = input()

if command == 'even':
    print(even)
elif command == 'odd':
    print(odds)
elif command == 'positive':
    print(pos)
else:
    print(neg)
