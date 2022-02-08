numbers_list = input().split()
n = int(input())

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

for i in range(n):
    min_el = min(numbers_list)
    numbers_list.remove(min_el)

for i in range(len(numbers_list)):
    numbers_list[i] = str(numbers_list[i])

print(', '.join(numbers_list))

****
numbers_int_list = [int(x) for x in numbers_list]
print(' > '.join([str(x) for x in numbers_int_list]))
