party_size = int(input())
days = int(input())

coins = 0
companian =party_size

for i in range(1, days+1):
    if i % 10 == 0:
        companian -= 2

    if i % 15 == 0:
        companian += 5

    if i %3 ==0:
        coins -= 3 * companian

    if i %5 == 0:
        coins += 20 * companian
        if i %3 == 0:
            coins -= 2 * companian

    coins += 50 - 2*companian

profit = int(coins/companian)

print(f'{companian} companions received {profit} coins each.')