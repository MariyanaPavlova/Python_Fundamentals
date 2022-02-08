# list1 = input().split(', ')
# list2 = input().split(', ')
# new = []
# x = [x for i in list2 for x in list1 if x in i ]
#
# print(sorted(set(x)))

find = input().split(", ")
here = input().split(", ")
result = []

for i_find in find:
    for i_here in here:
        if i_find in i_here:
            result.append(i_find)
result = list(dict.fromkeys(result))
print(result)
