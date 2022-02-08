def loading_bar(num):
    n_10 = num/10
    list = []

    for i in range(1,10+1):
        if i<= n_10:
            list.append('%')
        else:
            list.append('.')

    l =''.join(list)

    if num < 100:
        print(f'{n}% [{l}]')
        print(f'Still loading...')
    if num==100:
        print(f'{n}% Complete!')
        print(f'[{l}]')

n = int(input())
loading_bar(n)