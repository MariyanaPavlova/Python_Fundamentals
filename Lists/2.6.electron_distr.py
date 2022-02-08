el = int(input())
list = []
filled = 0

for i in range(1, el+1):
    shell = 2*(i**2)
    filled += shell
    if filled <= el:
        list.append(shell)
    else:
        filled -= shell
        break

add = el-filled
if add < el and add !=0:
    list.append(add)

print(list)
