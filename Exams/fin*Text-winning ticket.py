tickets = input().replace(" ", "")
tickets = tickets.split(',')
count = 0
symb = ''


def check_next(symbol, first, second):
    back = 6
    for i in range(7, 11):
        if (i * symbol) in first and (i * symbol) in second:
            back += 1
    return back


for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')
        continue
    left = ticket[0:int(len(ticket) / 2)]
    right = ticket[int(len(ticket) / 2):]

    if (6 * '@') in left and (6 * '@') in right:
        count = check_next('@', left, right)
        symb = '@'
    elif (6 * '$') in left and (6 * '$') in right:
        count = check_next('$', left, right)
        symb = '$'
    elif (6 * '#') in left and (6 * '#') in right:
        count = check_next('#', left, right)
        symb = '#'
    elif (6 * '^') in left and (6 * '^') in right:
        count = check_next('^', left, right)
        symb = '^'
    else:
        print(f'ticket "{ticket}" - no match')
        continue

    if count != 10:
        print(f'ticket "{ticket}" - {count}{symb}')
    else:
        print(f'ticket "{ticket}" - {count}{symb} Jackpot!')


# from re import findall
#
# ticket = input().split(",")
# ticket_ = "".join(ticket)
# ticket_in = ticket_.split()
#
# #tickets = [ticket.strip() for ticket in input().split(", ")]
#
# win = r'\@{6,10}|\${6,10}|\#{6,10}|\^{6,10}'
# jackpot = r'\@{20}|\${20}|\#{20}|\^{20}'
#
# for el in ticket_in:
#     if not len(el) == 20:
#         print(f"Invalid ticket")
#         continue
#
#     else:
#         right = el[0:10]
#         left = el[10:]
#
#         check_right = findall(win, right)
#         check_left = findall(win, left)
#         check_jackpot = findall(jackpot, el)
#
#         if check_jackpot:
#             print(f'f"ticket "{el}" - 10{el[0]} Jackpot!"')
#
#         elif check_left and check_right:
#             lenght = min(len(check_right[0]), len(check_left[0]))
#             print(f"ticket '{el}' - {lenght}{check_right[0][0]}")
#         else:
#             print(f'ticket "{el} - no match')
