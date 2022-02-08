words = input().split(' ')

dict = {}

for word in words:
    word_l = word.lower()
    if word_l not in dict:
        key = word_l
        value = 1
        dict[key] = value
    else:
        key = word_l # - ако не се сложи сумира върху посл.ел
        #value += 1  - ако го има изкривява сумата
        dict[key] += 1

for key,value in dict.items():
    if value %2!=0:
        print(key, end=' ')

