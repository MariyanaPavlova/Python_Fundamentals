neigborhood = [int(i) for i in input().split('@')]
command = input()
position = 0

while not command == 'Love!':
    curr_comm = command.split(' ')

    length_jump = int(curr_comm[-1])
    position += length_jump

    if position >= len(neigborhood):
        position = 0

    if neigborhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")

    else:
        neigborhood[position] -=2

        if neigborhood[position] ==0:
            print(f"Place {position} has Valentine's day.")

    command = input()
print(f"Cupid's last position was {position}.")

not_val_day =0

for i in neigborhood:
    if i !=0:
        not_val_day+=1

if not_val_day ==0:
    print('Mission was successful.')
else:
    print(f"Cupid has failed {not_val_day} places.")