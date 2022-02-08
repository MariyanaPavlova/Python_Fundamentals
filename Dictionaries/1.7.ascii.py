character = input().split(', ')

dict ={}

dict = {word: ord(word) for word in character}

# for word in character:
#     if word not in dict:
#         key = word
#         value = ord(word)
#         dict[key] = value

print(dict)