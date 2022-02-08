n = input().split(', ')
beggars = int(input())

summ = 0
amount = []
start_index = 0

for i in range(beggars):
    summ = 0

    for j in range(start_index, len(n), beggars):
        summ += int(n[j])

    amount.append(summ)
    start_index += 1
print(amount)

