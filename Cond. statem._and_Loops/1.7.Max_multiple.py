divisor = int(input())
bound = int(input())

n=0

for i in range(divisor, bound+1):
    result = i // divisor
    if i >0 and i <= bound and i % divisor ==0:

        n = i
print(n)