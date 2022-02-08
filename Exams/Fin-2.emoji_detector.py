import re

text = input()

pattern = r"(:{2}|\*{2})([A-Z]{1}[a-z]{2,})(\1)"
pattern_num = r"\d"

numbers = re.findall(pattern_num, text)
threshold = 1

for i in numbers:
    threshold *= int(i)
print(f'Cool threshold: {threshold}')

# for digits in text:  - може и с isdigit в целия текст
#     if digits.isdigit():
#         threshold *= int(digits)

emoji = re.findall(pattern, text)
if len(emoji) > 0:
    print(f'{len(emoji)} emojis found in the text. The cool ones are:')

    for el in emoji:
        emoji_point = 0
        for char in el[1]:
            emoji_point += ord(char)
        if emoji_point >= threshold:
            print("".join(el))

# import re
#
# pattern = r"(?P<surr>\:\:|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=surr)"
# pattern_numbers = r"\d"
# text = input()
#
# all_numbers_in_text_as_strings = re.findall(pattern_numbers, text)
# all_numbers_as_integers = [int(num_str) for num_str in all_numbers_in_text_as_strings]
#
# threshold = 1
# for num in all_numbers_as_integers:
#     threshold *= num
#
# emoji_matches = re.finditer(pattern, text)
# print(f"Cool threshold: {threshold}")
#
# emojis_to_print = []
#
# emoji_count = 0
# for match in emoji_matches:
#     emoji_count += 1
#     data = match.groupdict()
#     emoji = data["emoji"]
#     emoji_coolnes = sum([ord(letter) for letter in emoji])
#
#     if emoji_coolnes >= threshold:
#         emojis_to_print.append(f"{data['surr']}{data['emoji']}{data['surr']}")
#
# print(f"{emoji_count} emojis found in the text. The cool ones are:")
# # print("\n".join(emojis_to_print))
# for emoji in emojis_to_print:
#     print(emoji)