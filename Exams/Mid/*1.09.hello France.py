item = input().split('|')
budget = int(input())

new = []
new_price=0
profit=0
summ=0

for i in item:
    curr_item = i.split('->')
    tipe = curr_item[0]
    price = float(curr_item[-1])

    if tipe == 'Clothes'and price <= 50.00 and budget >= price:
        budget -= price
        new.append(price)

    elif tipe == 'Shoes' and price <= 35.00 and budget >= price:
        budget -= price
        new.append(price)

    elif tipe == 'Accessories' and price <= 20.50 and budget >= price:
        budget -= price
        new.append(price)

for j in new:
    profit += float(j) * 0.40
    new_price = float(j) * 1.40
    summ += new_price
    print(f'{new_price:.2f}', end=" ")

print()
print(f'Profit: {profit:.2f}')
if summ + budget >= 150:
    print(f'Hello, France!')
else:
    print(f'Time to go.')
