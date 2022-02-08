command = input()

products_price = {}
products_qty = {}

while not command == 'buy':
    name, price, quantity = command.split(' ')
    price = float(price)
    qty = int(quantity)

    if name not in products_price:
        products_price[name] = price
        products_qty[name] = qty
    else:
        products_price[name] = price
        products_qty[name] += qty

    command = input()

for product, price in products_price.items():
    result = price * products_qty[product]
    print(f'{product} -> {result:.2f}')