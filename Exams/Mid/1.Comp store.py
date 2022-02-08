price_part = input()

price = 0

while not (price_part == 'special' or price_part == 'regular'):
    if float(price_part) < 0:
        print('Invalid price!')
        pass
    else:
        price += float(price_part)

    price_part = input()

if price ==0:
    print('Invalid order!')
    exit()

taxes = price *0.20
final_price = price + taxes

print("Congratulations you've just bought a new computer!")
print(f'Price without taxes: {price:.2f}$')
print(f'Taxes: {taxes:.2f}$')
print('-----------')
if price_part == 'special':
    disc_price = final_price- final_price*0.10
    print(f'Total price: {disc_price:.2f}$')
else:
    print(f'Total price: {final_price:.2f}$')




