n = int(input())
count = int(input())
a = n*count
list=[]

for i in range(n, a+1, n):
    list.append(i)
print(list)