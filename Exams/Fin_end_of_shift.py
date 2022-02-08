import re

pattern = r'%([A-Z][a-z]+)%[^<]*?<([^>]*?)>[^\|]*?\|(\d+)\|[^\d]*?(\d+\.\d+)'

command = input()
sum_of_all = 0
while not command == "end of shift":
    match = re.search(pattern, command)

    if match:
        name, product, quantity, price = match.groups()
        total_price = int(quantity) * float(price)
        sum_of_all += total_price
        print(f"{name}: {product} - {total_price:.2f}")

    command = input()

print(f'Total income: {sum_of_all:.2f}')


# import re
# command = input()
# total_price = 0
# while command != "end of shift":
#     current_price = 0
#     pattern = r'%([A-Z][a-z]+)%[^\|\$%\.]*?<(\w+)>[^\|\$%\.]*?\|(\d+)\|.*?(\d+\.?\d+)\$'
#     if re.search(pattern, command):
#         name, product, quantity, price = re.search(pattern, command).groups()
#         current_price = int(quantity) * float(price)
#         print(f'{name}: {product} - {current_price:.2f}')
#         total_price += current_price
#     command = input()
# print(f'Total income: {total_price:.2f}')
#
