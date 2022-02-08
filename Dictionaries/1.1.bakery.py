data = input().split(' ')

product = {}
for i in range(0, len(data), 2):
    key = data[i]
    value = int(data[i+1])
    product[key] = value

print(product)