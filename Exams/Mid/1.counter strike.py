energy = int(input())
won = 0

while True:
    command = input()

    if command == 'End of battle':
        print(f"Won battles: {won}. Energy left: {energy}")
        break

    if energy >= int(command):
        energy -= int(command)
        won +=1
    else:
        print(f"Not enough energy! Game ends with {won} won battles and {energy} energy")
        break

    if won %3 ==0:
        energy += won


