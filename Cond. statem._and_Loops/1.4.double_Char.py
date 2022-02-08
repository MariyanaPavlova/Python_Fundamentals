text = input()

double= ''

'''for i in range(0, len(text)):
    double += text[i]+text[i]
print(double)'''

for i in text:
    print(i*2, end='')