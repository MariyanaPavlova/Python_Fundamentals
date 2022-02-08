elements = input().split()
line = input()
moves = 0

while not line == "end" and len(elements) > 0:
    moves += 1
    first_index, second_index = line.split()
    first_index = int(first_index)
    second_index = int(second_index)

    middle = len(elements) // 2
    if not 0 <= first_index < len(elements) or not 0 <= second_index < len(elements):
        elements.insert(middle, "-" + str(moves) + "a")
        elements.insert(middle, "-" + str(moves) + "a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if elements[first_index] == elements[second_index]:
            print(f"Congrats! You have found matching elements - {elements[first_index]}!")
            if first_index > second_index:
                elements.pop(first_index)
                elements.pop(second_index)
            else:
                elements.pop(second_index)
                elements.pop(first_index)
        else:
            print("Try again!")
    line = input()

if len(elements) > 0:
    print("Sorry you lose :(")
    print(" ".join(elements))
else:
    print(f"You have won in {moves} turns!")