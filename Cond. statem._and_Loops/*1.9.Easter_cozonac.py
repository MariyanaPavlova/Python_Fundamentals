budget = float(input())
flour = float(input())

eggs = flour * 0.75
milk = (flour + (flour *0.25)) * 0.250

count_coz = 0
colored_eggs = 0

price_1coz = flour + eggs + milk

while budget - price_1coz >= 0:
    budget -= price_1coz
    colored_eggs +=3
    count_coz += 1
    if count_coz %3 ==0:
        colored_eggs -= (count_coz-2)

left_money = budget
print(f'You made {count_coz} cozonacs! Now you have {colored_eggs} eggs and {left_money:.2f}BGN left.')
