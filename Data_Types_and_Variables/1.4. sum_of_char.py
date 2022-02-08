n = int(input())
num=0

for i in range(n):
    letter = input()
    num += ord(letter)
print(f'The sum equals: {num}')
