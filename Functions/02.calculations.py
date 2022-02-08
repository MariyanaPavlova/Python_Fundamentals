oper1 = input()
a1 = int(input())
b1 = int(input())


def calculation(oper, a, b):
    if oper == 'multiply':
        return a * b
    elif oper == 'divide':
        return a // b
    elif oper == 'add':
        return a + b
    elif oper == 'subtract':
        return a - b

print(calculation(oper1, a1, b1))