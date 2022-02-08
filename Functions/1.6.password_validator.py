def valid_pass(n):

    digit=0
    character = 0
    other=0
    valid=0
    invalid=0
    for i in n:
        if 48<=ord(i) <=57:
            digit += 1
        elif 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            character +=1
        else:
            
            other+=1

    if 6<=len(n)<=10:
        valid +=1
    else:
        invalid+=1
        print(f'Password must be between 6 and 10 characters')
    if other !=0:
        invalid+=1
        print(f'Password must consist only of letters and digits')
    if digit >=2:
        valid +=1
    else:
        invalid+=1
        print(f'Password must have at least 2 digits')
    if character >=0:
        valid +=1

    if valid>=3 and invalid ==0:
        print(f'Password is valid')
n = input()

valid_pass(n)
