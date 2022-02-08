data = input()

bake = {}
sold = {}
new_dict = {}

while not data == "Complete":
    data = data.split(" ")
    command = data[0]
    quant = int(data[1])
    food = data[2]

    if command == "Receive":
        if quant > 0:
            if food not in bake:
                bake[food] = quant
            else:
                bake[food] += quant
        else:
            continue
    elif command == "Sell":
        if food not in bake:
            print(f'You do not have any {food}.')
        else:

            if bake[food] >= quant:
                bake[food] -= quant
                print(f"You sold {quant} {food}.")
                sold[food] = quant

                if bake[food] == 0:
                    del bake[food]

            elif bake[food] < quant:
                if food not in sold:
                    sold[food] = bake[food]
                    bake[food] =0

                del bake[food]
                print(f"There aren't enough {food}. You sold the last {(sold[food])} of them.")

    data = input()
sorted_bake = (sorted(bake.items(), key=lambda x: (x[0], x)))
for key, value in sorted_bake:
    print(f'{key}: {value}')
summ = 0
for k, v in sold.items():
    summ += v
print(f'All sold: {summ} goods')
