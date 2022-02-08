journal = input().split(', ')
craft = input()

while not craft == 'Craft!':
    craft_sp = craft.split(' - ')
    do = craft_sp[0]
    thing = craft_sp[-1]

    if do == 'Collect':
        if thing in journal:
            pass
        else:
            journal.append(thing)

    elif do == 'Drop':
        if thing in journal:
            journal.remove(thing)
        else:
            pass

    elif do == 'Combine Items':
        comb = thing.split(':')
        old = comb[0]
        new = comb[1]
        if old in journal:
            ind=int(journal.index(old))
            journal.insert(ind+1, new)

    elif do == 'Renew':
        if thing in journal:
            journal.remove(thing)
            journal.append(thing)


    craft = input()

print(', '.join(journal))
