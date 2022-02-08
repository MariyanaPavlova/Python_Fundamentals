product = input()
quantity = int(input())

def calculate(a,b):
    if product == 'coffee':
        return 1.50 * quantity
    elif product == 'water':
        return 1.00 * quantity
    elif product == 'coke':
        return 1.40 * quantity
    elif product == 'snacks':
        return  2.00 * quantity


result = calculate(product, quantity)
print(f'{result:.2f}')