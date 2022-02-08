list = input()

a=list.split(' ')
n=[]

for i in a:
    n.append(int(i) * -1)
print(n)
