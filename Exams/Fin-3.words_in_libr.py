
words_and_definitions = input().split(" | ")
my_dict = {}
print1 = []
for ele in words_and_definitions:
    single = ele.split(":")
    word = single[0]
    definition = single[1]
    definition1 = definition[1:]
    if word not in my_dict:
        my_dict[word] = [definition1]
    else:
        my_dict[word].append(definition1)

words = input().split(" | ")
end_command = input()

if end_command == "Test":
    for ele in words:
        if ele in my_dict:
            print(f"{ele}:")
            x = sorted(my_dict[ele], key=len)
            x.reverse()
            for v in x:
                print(f" -{''.join(v)}")
else:
    for i in sorted(my_dict.keys()):
        print1.append(i)
    print(' '.join(print1))