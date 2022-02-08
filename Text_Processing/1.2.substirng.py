word = input().split()

result = ""

for i in word:
    result += i * len(i)

print(result)
