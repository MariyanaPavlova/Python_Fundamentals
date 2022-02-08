n = int(input())
word = input()

listt= []
new_listt = []

for i in range(n):
    sentance = input()
    listt.append(sentance)

for i in range(len(listt)): # ще работи и без този for
    if word in listt[i]:
        new_listt.append(listt[i])

print(listt)
print(new_listt)
