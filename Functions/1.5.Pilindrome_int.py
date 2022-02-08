def check_if_palindrome(el):
    if el == el[::-1]:
        return True
    return False

num=input().split(', ')

for i in num:
    print(check_if_palindrome(i))

