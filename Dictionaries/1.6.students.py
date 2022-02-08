data = input()
curses = {}

while ':' in data:
    student_name, id, curse_name = data.split(':')
    if curse_name not in curses:
        curses[curse_name] = {}
    curses[curse_name][id] = student_name

    data = input()

searched_curses = data
searched_curses = searched_curses.replace('_', ' ')

for i in curses:
    if i == searched_curses:
        for id, name in curses[i].items():
            print(f'{name} - {id}')

