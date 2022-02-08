def oddeven(n):

    even = 0
    odd = 0

    for i in num:
        sell = int(i)
        if sell % 2 == 0:
            even += sell
        else:
            odd += sell
    # return f'Odd sum = {odd}, Even sum = {even}'
    return [even, odd]

num = input()

result = oddeven(num)
# print(result)

even_sum = result[0]
odd_sum = result[1]
print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')