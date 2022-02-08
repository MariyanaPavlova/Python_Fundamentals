data = input().split(' ')
search = input().split(' ')

product = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = int(data[i+1])
    product[key]=value
for j in search:
    if j in product:
        print(f"We have {product[j]} of {j} left")
    else:
        print(f"Sorry, we don't have {''.join(j)}")
