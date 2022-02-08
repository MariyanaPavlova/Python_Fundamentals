text = input()

text_repl = text.replace(' ', '')
dict = {}

for letter in text_repl:

    if letter not in dict:
        key = letter
        value = 1
        dict[key] = value
    else:
        key = letter
        dict[key] += 1

for key, value in dict.items():
    print(f'{key} -> {value}')



# input_text = input()
#
# result_dict = {}
#
# for char in input_text:
#     if char != " ":
#         result_dict[char] = input_text.count(char)
#
# print('\n'.join('{} -> {}'.format(key, value) for (key, value) in result_dict.items()))