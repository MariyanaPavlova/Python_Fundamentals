import string

data = input().split()

total = 0
for i in range(len(data)):
    first_letter = data[i][0]
    second_letter = data[i][-1]
    numb = int(data[i][1:-1])

    first_letter_pos = string.ascii_lowercase.index(first_letter.lower())+1
    second_letter_pos = string.ascii_lowercase.index(second_letter.lower())+1

    if first_letter.isupper():
        numb = numb/first_letter_pos
    else:
        numb *= first_letter_pos

    if second_letter.isupper():
        numb -= second_letter_pos
    else:
        numb += second_letter_pos

    total += numb

print(f'{total:.2f}')

#print(string.ascii_lowercase.index(a))
