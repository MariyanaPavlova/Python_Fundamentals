def check_item_exists(item_list, item):
    if item in item_list:
        return True
    return False

def add_item(item_list, item):
    if not check_item_exists(item_list, item):
        item_list.append(item)
    return item_list

def remove_item(item_list, item_data):
    if check_item_exists(item_list, item):
        item_list.remove(item)
    return item_list

def combine_item(item_list, items_data):
    old_item, new_item = items_data.split(':')
    if check_item_exists(item_list, old_item):
        index_old_item = item_list.index(old_item)
        item_list.insert(index_old_item+1, new_item)
    return item_list

def renew_item(item_list, item):
    if check_item_exists(item_list, item):
        item_list.remove(item)
        item_list.append(item)
    return item_list


items = input().split(', ')
command_data = input()

while not command_data == 'Craft!':
    command, item = command_data.split(' - ')
    if command == 'Collect':
        items = add_item(items, item)
    elif command == 'Drop':
        items = remove_item(items, item)
    elif command == 'Combine Items':
        items = combine_item(items, item)
    elif command == 'Renew':
        items = renew_item(items, item)

    command_data = input()
for i in range(len(items)):
    if i == len(items)-1:
        print(f'{items[i]}')
    else:
        print(f'{items[i]}, ', end='')

