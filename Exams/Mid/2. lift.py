people_waiting = int(input())

cabins = [int(i) for i in input().split(' ')]

empty=0

for i in range(len(cabins)):
    if cabins[i] <= 4 and people_waiting > 0:
        people_waiting -= 4 - cabins[i]

        if people_waiting > 0:
            cabins[i] += 4 - cabins[i]
        elif people_waiting <=0:
            cabins[i] += (4+people_waiting) - cabins[i]
            empty =1

if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")

if people_waiting <= 0 and empty ==1:
    print("The lift has empty spots!")

print(*cabins, sep=" ")