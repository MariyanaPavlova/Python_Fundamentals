import re
text = input()
pattern = r'(#|@)([A-Za-z)]{3,})\1(#|@)([A-Za-z)]{3,})\1'

matched = re.finditer(pattern,text)
#matched= re.findall(pattern, text)
count = 0
miror_word=[]

for el in matched:
#for i in range(len(matched)):
    count +=1
    word_1= el.group(2)
    word_2= el.group(4)
    #word_1 = matched[i][1]
    #word_2 = matched[i][3]
    back = word_2[::-1]

    if word_1 == back:

        miror_word.append(f'{word_1} <=> {word_2}')

if count == 0:
    print("No word pairs found!")
else:
    print(f"{count} word pairs found!")

if len(miror_word)==0:
    print('No mirror words!')
else:
    print(f'The mirror words are:')
    print(", ".join(miror_word))

