list = input().split(', ')
list_int = [int(x) for x in list]
new=[]
#
# for index, i in enumerate(list):
#     if int(i)%2==0:
#         new.append(index)
# print(new)
#

for i in range(len(list_int)):
    if list_int[i] %2==0:
        new.append(i)
print(new)