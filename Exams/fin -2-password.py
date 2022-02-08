import re

number_of_passwords = int(input())

pattern = r'(?P<separator>.+)>(?P<first>[0-9]{3})\|(?P<second>[a-z]{3})\|(?P<third>[A-Z]{3})\|(?P<fourth>[^<>]{3})<(?P=separator)'

for i in range(number_of_passwords):
    text = input()

    match = re.search(pattern, text)

    if match:
        print(
            f"Password: {match.group('first') + match.group('second') + match.group('third') + match.group('fourth')}")
    else:
        print("Try another password!")