strings = input().split(" ")
str_a = strings[0]
str_b = strings[1]

sum = 0

for i in range(len(str_a)):

    if i < len(str_b):
        sum += ord(str_a[i]) * ord(str_b[i])
    if i >= len(str_b):
        sum += ord(str_a[i])

for j in range(len(str_a), len(str_b)):
    sum += ord(str_b[j])
print(sum)
