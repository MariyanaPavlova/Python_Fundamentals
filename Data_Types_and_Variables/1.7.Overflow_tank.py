n = int(input())

capacity = 255
pour = 0

for i in range(n):
    liters = int(input())
    pour += liters

    if pour > capacity or liters > capacity:
        print(f'Insufficient capacity!')
        pour -= liters

print(f'{pour}')
