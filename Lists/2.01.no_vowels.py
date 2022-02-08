# text = input()
# new = ''
# new_p=''
# for i in text:
#     if i=='a' or i=='o' or i=='e' or i=='u' or i=='i':
#         new += i
#     else:
#         new_p +=i
# print(new_p)

vowel = ['a', 'e', 'o', 'u', 'i']
text = input()
x = [i for i in text if i.lower() not in vowel]
print(''.join(x))