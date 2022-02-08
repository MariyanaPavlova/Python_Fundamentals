command = input()

dict = {}

while not command == "Sail":

    command=command.split("||")
    city = command[0]
    people = int(command[1])
    gold = int(command[2])

    if city not in dict:
        dict[city]= []
        dict[city].append(people)
        dict[city].append(gold)
    else:
        dict[city][0] += people
        dict[city][1] += gold

    command = input()

data = input()
while not data == "End":
    data = data.split("=>")

    if data[0] == "Plunder":
        city = data[1]
        people = int(data[2])
        gold = int(data[3])

        dict[city][0] -= people
        dict[city][1] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if dict[city][0] <=0 or dict[city][1] <= 0:
            del dict[city]
            #dict.pop(city)
            print(f'{city} has been wiped off the map!')


    elif data[0] == "Prosper":
        city = data[1]
        gold = int(data[2])
        if gold <0:
            print(f"Gold added cannot be a negative number!")

        else:
            dict[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {dict[city][1]} gold.")
    data = input()

sorted_dict = (sorted(dict.items(), key=lambda x: (-x[1][1], x)))
print(f'Ahoy, Captain! There are {len(dict)} wealthy settlements to go to:')
if len(dict) > 0:
    for key, value in sorted_dict:
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')

else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

