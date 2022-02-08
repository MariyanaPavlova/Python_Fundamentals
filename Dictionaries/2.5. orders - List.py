item = input()

dict = {}

while not item == 'buy':
    items = item.split(' ')
    prod_name = items[0]
    price = float(items[1])
    qty = int(items[2])

    if prod_name not in dict:
        # dict[prod_name] = [price, qty] - написано по др.начин
        dict[prod_name] = []
        dict[prod_name].append(price)
        dict[prod_name].append(qty)

    else:
        #dic[prod_name][0] = price - написано по др.начин
        #dict[prod_name][1] += qty
        for key, value in dict.items():
            if key == prod_name:
                value[0] = price
                value[1] += qty

    item = input()

for key, value in dict.items():
    print(f'{key} -> {(value[0] * value[1]):.2f}')