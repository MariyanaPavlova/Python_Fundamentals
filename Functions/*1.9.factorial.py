n = int(input())
n2 = int(input())

def sum_numbers(n, n2):
    fact = n
    div = n2
    for i in range(n,1,-1):
        fact *=(i-1)

    for i in range(n2,1,-1):
        div *=(i-1)

    subs = fact / div
    return subs

result = sum_numbers(n, n2)
print(f'{result:.2f}')
