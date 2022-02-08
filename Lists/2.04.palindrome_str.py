word = input().split(' ')
palindrom = input()
new_list = []

num = word.count(palindrom)
for i in word:
    if i==i[::-1]:
        new_list.append(i)
print(new_list)

print(f'Found palindrome {num} times')

