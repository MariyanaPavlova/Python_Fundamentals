command = input()

products = {}

while not command == 'buy':
    name, price, quantity = command.split(' ')
    price = float(price)
    qty = int(quantity)

    if name not in products:
        products[name] = {'price': price, 'quantity': qty}

    else:
        products[name]['quantity'] += qty
        products[name]['price'] = price

    command = input()

for key, value in products.items():
    result = value["price"] * value["quantity"]
    print(f'{key} -> {result:.2f}')