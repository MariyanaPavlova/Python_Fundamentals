n11 = input()
n22 = input()

def character(n1, n2):
    for i in range(ord(n1)+1, ord(n2)):
        print(chr(i), end=' ')

character(n11, n22)